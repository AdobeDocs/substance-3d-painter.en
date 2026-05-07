#!/usr/bin/env python3
"""
Normalize markdown pipe-table spacing in a folder of .md files.

Rules:
- Empty cells (only whitespace) become a single space between pipes: | | not |  |  |
- Every cell's content is wrapped with exactly one leading and one trailing space
  (except that an empty cell is a single space total).
- Trailing all-empty table rows (consecutive at the end of a pipe table block)
  are removed. The first/only row in a run is never dropped (typical empty
  header), and an empty row that has any non-table line below is never dropped
  because a blank line or non-pipe line ends the table and therefore that empty
  row is not a trailing run suffix.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

def _normalize_cell(raw: str) -> str:
    t = raw.strip()
    if not t:
        return " "
    return f" {t} "


def _parse_gfm_table_row(
    line: str,
) -> tuple[str, str, list[str]] | None:
    """
    If line is a single-line GFM-style pipe table row, return
    (eol, lead_whitespace, cells). Cells are raw strings, with spurious
    trailing empty column cells already removed.
    """
    if line.endswith("\r\n"):
        eol, body = "\r\n", line[:-2]
    elif line.endswith("\n"):
        eol, body = "\n", line[:-1]
    else:
        eol, body = "", line

    lead_ws_len = len(body) - len(body.lstrip(" \t"))
    leadin = body[:lead_ws_len]
    t = body[lead_ws_len:].rstrip()
    if not t.startswith("|") or t.count("|") < 2:
        return None

    if t.endswith("|"):
        between = t[1:-1]  # content strictly between the outermost pipes
        cells = between.split("|")
    else:
        parts = t.split("|")
        if parts[0] != "":
            return None
        cells = parts[1:]

    # Remove spurious trailing empty cells (e.g. an extra column from a
    # previous bad parse, or a trailing " |" that became an extra cell).
    while len(cells) > 2 and not cells[-1].strip():
        cells.pop()

    return (eol, leadin, cells)


def _is_fully_empty_table_row(line: str) -> bool:
    """True if the row parses as a GFM table and every cell is whitespace only."""
    parsed = _parse_gfm_table_row(line)
    if parsed is None:
        return False
    _, _, cells = parsed
    if not cells:
        return True
    return not any(c.strip() for c in cells)


def _remove_trailing_empty_table_rows(run: list[str]) -> list[str]:
    """
    Drop empty rows at the end of a contiguous GFM table run. Keeps a single
    remaining empty row (e.g. empty header) when the run would otherwise
    become empty, or the only line left is that empty line.
    """
    out = list(run)
    while len(out) > 1 and _is_fully_empty_table_row(out[-1]):
        out.pop()
    return out


def fix_table_line(line: str) -> str | None:
    """
    If the line is a single-line pipe table, return a normalized version.
    Otherwise return None (caller should keep the original line).

    Parses cells as the substrings *between* the first and last ``|`` on
    the row when the row ends with ``|``; a trailing ``|?`` in regex is unsafe
    here because optional matching lets ``.+`` swallow an extra ``|`` and
    create a spurious extra column (e.g. two-column ``|  |  |`` would become
    three cells).
    """
    parsed = _parse_gfm_table_row(line)
    if parsed is None:
        return None
    eol, leadin, cells = parsed
    normalized = [_normalize_cell(c) for c in cells]
    new_body = leadin + "|" + "|".join(normalized) + "|"
    return new_body + eol


def is_gfm_table_line(line: str) -> bool:
    """True if the line is parsed as a GFM pipe table row (normalized or not)."""
    return _parse_gfm_table_row(line) is not None


def transform_file_text(text: str) -> tuple[str, bool]:
    """
    Pass 1: normalize GFM table cell spacing outside fenced code.
    Pass 2: in those same regions, remove consecutive all-empty rows at
    the end of each run of GFM table lines. Compare final string to the
    original ``text`` to set the changed flag.
    """
    orig_lines = text.splitlines(keepends=True)
    in_fence = False
    stage1: list[str] = []
    for line in orig_lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            stage1.append(line)
            continue
        if in_fence:
            stage1.append(line)
            continue
        fixed = fix_table_line(line)
        stage1.append(fixed if fixed is not None else line)

    in_fence = False
    out: list[str] = []
    k, n = 0, len(stage1)
    while k < n:
        ln = stage1[k]
        if ln.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            k += 1
            continue
        if in_fence:
            out.append(ln)
            k += 1
            continue
        if not is_gfm_table_line(ln):
            out.append(ln)
            k += 1
            continue
        j = k
        while j < n and is_gfm_table_line(stage1[j]):
            j += 1
        run = stage1[k:j]
        out.extend(_remove_trailing_empty_table_rows(run))
        k = j

    result = "".join(out)
    return result, result != text


def process_file(path: Path) -> bool:
    """Read file, apply ``transform_file_text``; return True if content changed."""
    text = path.read_text(encoding="utf-8")
    new, changed = transform_file_text(text)
    if changed:
        path.write_text(new, encoding="utf-8", newline="")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fix pipe-table cell spacing in markdown files."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path("help/painting/generators"),
        help="Directory of .md files (default: help/painting/generators)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files that would change without writing",
    )
    args = parser.parse_args()
    root: Path = args.path
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 1

    md_files = sorted(root.rglob("*.md"))
    would_change: list[Path] = []
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        _, changed = transform_file_text(text)
        if changed:
            would_change.append(f)

    if args.dry_run:
        for f in would_change:
            print(f)
        print(f"Would update {len(would_change)} file(s).", file=sys.stderr)
        return 0

    changed: list[Path] = []
    for f in md_files:
        if process_file(f):
            changed.append(f)

    for f in changed:
        print(f"Updated: {f}")
    print(f"Done. {len(changed)} file(s) updated.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
