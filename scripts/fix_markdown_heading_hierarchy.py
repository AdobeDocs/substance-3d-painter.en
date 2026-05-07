#!/usr/bin/env python3
"""
Fix ATX heading levels in Markdown so levels are never "skipped" (e.g. ## then ####).
The logical parent of each heading is at most one level above. Repeated same raw
level (e.g. many #### under one ##) are corrected to the same level as peers, not
nested as children of the first.

Ignored: YAML front matter (--- ... ---), fenced code (```/~~~), and lines
inside a top-level HTML <table> ... </table> block.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_ATX = re.compile(r"^(?P<ind> {0,3})(?P<hs>#{1,6})(?=\s|$)(?P<rest>.*)$")


def _atx_level(line: str) -> int | None:
    m = _ATX.match(line.rstrip("\n"))
    if not m:
        return None
    return len(m.group("hs"))


def _rebuild_line(line: str, new_n: int) -> str:
    s = line
    eol = ""
    if s.endswith("\r\n"):
        eol, s = "\r\n", s[:-2]
    elif s.endswith("\n"):
        eol, s = "\n", s[:-1]
    m = _ATX.match(s)
    if not m or new_n < 1 or new_n > 6:
        return line
    return f"{m.group('ind')}{'#' * new_n}{m.group('rest')}{eol}"


def _table_line_delta(line: str) -> int:
    o = len(re.findall(r"(?i)<\s*table(?=[\s>])", line))
    c = len(re.findall(r"(?i)</\s*table", line))
    return o - c


def _front_matter_range(lines: list[str]) -> range | None:
    n = len(lines)
    if n and lines[0].strip() == "---":
        for j in range(1, n):
            if lines[j].strip() == "---":
                return range(0, j + 1)
    return None


def _collect_atx(
    lines: list[str], fm: range | None
) -> list[tuple[int, int]]:
    skip: set[int] = set(fm) if fm is not None else set()
    in_fence = False
    tdepth = 0
    out: list[tuple[int, int]] = []
    for i, line in enumerate(lines):
        if i in skip:
            continue
        if line.lstrip().startswith("```") or line.lstrip().startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        tdepth = max(0, tdepth + _table_line_delta(line))
        if tdepth > 0:
            continue
        le = _atx_level(line)
        if le is not None:
            out.append((i, le))
    return out


def _corrected_levels(levels: list[int]) -> list[int]:
    stack: list[int] = []
    out: list[int] = []
    prev_r: int | None = None
    prev_t: int | None = None
    prev_gap: bool = False
    for r in levels:
        w = list(stack)
        while w and w[-1] >= r:
            w.pop()
        if prev_r is not None and r == prev_r and prev_gap and prev_t is not None:
            while w and w[-1] >= prev_t:
                w.pop()
        if not w:
            t = r
        else:
            p = w[-1]
            t = p + 1 if r > p + 1 else r
        if prev_r is not None and r == prev_r and prev_t is not None:
            t = prev_t
        out.append(t)
        gap = bool(w) and r > w[-1] + 1
        while stack and stack[-1] >= t:
            stack.pop()
        stack.append(t)
        prev_r, prev_t, prev_gap = r, t, gap
    return out


def transform_text(
    text: str,
) -> tuple[str, bool, list[str]]:
    lines = text.splitlines(keepends=True)
    fm = _front_matter_range(lines)
    col = _collect_atx(lines, fm)
    if not col:
        return text, False, []
    old_l = [lv for _i, lv in col]
    new_l = _corrected_levels(old_l)
    notes: list[str] = []
    any_ = any(a != b for a, b in zip(old_l, new_l, strict=True))
    if not any_:
        return text, False, []
    for k, ((idx, o), t) in enumerate(zip(col, new_l, strict=True)):
        if o != t:
            s = lines[idx].rstrip()[:64]
            notes.append(f"line {idx + 1}: {o}->{t}  {s}")
    for k in range(len(col) - 1, -1, -1):
        idx, o = col[k]
        t = new_l[k]
        if t == o:
            continue
        lines[idx] = _rebuild_line(lines[idx], t)
    return "".join(lines), True, notes


def process_file(path: Path) -> tuple[bool, list[str]]:
    raw = path.read_text(encoding="utf-8")
    new, ch, notes = transform_text(raw)
    if ch and new != raw:
        path.write_text(new, encoding="utf-8", newline="")
    return (ch, notes)


def _rel(p: Path, base: Path) -> str:
    try:
        return str(p.resolve().relative_to(base))
    except ValueError:
        return str(p)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Fix ATX heading hierarchy: no skipped levels; same-#### peers under same ## stay peers.",
    )
    ap.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path("help/painting/generators"),
        help="Root to scan for *.md (default: help/painting/generators).",
    )
    ap.add_argument("--dry-run", action="store_true", help="Show diffs, do not write.")
    ap.add_argument("--quiet", action="store_true", help="Minimal one-line output.")
    args = ap.parse_args()
    root = args.path
    if not root.is_dir():
        print(f"Not a directory: {root.resolve()}", file=sys.stderr)
        return 1
    base = root.resolve()
    mds = sorted(root.rglob("*.md"))
    to_alter: list[tuple[Path, list[str], str]] = []
    for p in mds:
        t = p.read_text(encoding="utf-8")
        n, ch, notes = transform_text(t)
        if ch and n != t:
            to_alter.append((p, notes, n))
    if args.dry_run:
        n_files = 0
        n_edits = 0
        for p, notes, _n in to_alter:
            n_files += 1
            n_edits += len(notes)
        if not args.quiet:
            print("fix_markdown_heading_hierarchy (dry run - no writes)")
            print(f"  root: {base}")
            print(f"  .md count: {len(mds)}")
            print()
        for p, notes, _n in to_alter:
            if not args.quiet:
                print(f"  {_rel(p, base)}: {len(notes)} heading(s) to retarget")
                for s in notes[:20]:
                    print(f"    {s}")
                if len(notes) > 20:
                    print(f"    ... and {len(notes) - 20} more")
        if not args.quiet and to_alter:
            print()
            print(
                f"Summary: {n_files} file(s) with changes, {n_edits} heading line(s) total. "
                f"({len(mds) - n_files} files unchanged.)"
            )
        if not args.quiet and not to_alter:
            print("  No heading retargets needed in any file.")
        if args.quiet:
            if to_alter:
                print(
                    f"Would edit {len(to_alter)} file(s) ({n_edits} heading line(s))."
                )
            else:
                print("No heading fixes needed.")
        return 0
    changed = 0
    for p in mds:
        w, nts = process_file(p)
        if w:
            changed += 1
            if not args.quiet:
                print(f"Updated: {_rel(p, base)}  ({len(nts)} heading(s))")
    if not args.quiet:
        print(
            f"Done. {changed} of {len(mds)} file(s) written."
        )
    else:
        print(
            f"fix_markdown_heading_hierarchy: {changed}/{len(mds)} file(s) written."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
