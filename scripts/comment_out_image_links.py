#!/usr/bin/env python3
"""
Comment out (or restore) image markup in markdown articles using HTML comments.

- Markdown: ``![alt](dest)`` and optional title in quotes
- HTML: ``<img ...>`` and ``<img .../>``

Fenced code blocks (`` ``` ``) are not modified. The default path is
``help/painting/generators`` (the new articles folder).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

# Whole-line HTML comment that wraps a single image (our format)
_WHOLE_COMMENT = re.compile(
    r"^(\s*)<!--\s*(.+?)\s*-->(\s*)$",
    re.DOTALL,
)
_IMG_TAG = re.compile(r"(?is)(<img\b[^>]+/?\s*>)")


def _md_image_spans(s: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    pos = 0
    while pos < len(s):
        p = s.find("![", pos)
        if p < 0:
            break
        rb = s.find("]", p + 2)
        if rb < 0 or rb + 1 >= len(s) or s[rb + 1] != "(":
            pos = p + 2
            continue
        i = rb + 2
        in_q: str | None = None
        while i < len(s):
            c = s[i]
            if in_q:
                if c == "\\" and i + 1 < len(s):
                    i += 2
                    continue
                if c == in_q:
                    in_q = None
                i += 1
                continue
            if c in ('"', "'"):
                in_q = c
                i += 1
                continue
            if c == ")":
                out.append((p, i + 1))
                pos = i + 1
                break
            i += 1
        else:
            pos = p + 2
    return out


def _html_img_spans(s: str) -> list[tuple[int, int]]:
    return [(m.start(1), m.end(1)) for m in _IMG_TAG.finditer(s)]


def _merge_spans(spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not spans:
        return []
    s = sorted(spans, key=lambda t: (t[0], -t[1]))
    merged: list[tuple[int, int]] = []
    for a, b in s:
        if not merged or a > merged[-1][1]:
            merged.append((a, b))
        else:
            la, lb = merged[-1]
            merged[-1] = (la, max(lb, b))
    return merged


def _wrap_in_comment(text: str) -> str:
    return f"<!-- {text} -->"


def comment_out_line(line: str) -> tuple[str, bool]:
    """Comment out each markdown image and HTML <img> on the line. Idempotent for our wrappers."""
    raw = line
    eol = ""
    if raw.endswith("\r\n"):
        body, eol = raw[:-2], "\r\n"
    elif raw.endswith("\n"):
        body, eol = raw[:-1], "\n"
    else:
        body, eol = raw, ""

    m_w = _WHOLE_COMMENT.match(body)
    if m_w and (
        m_w.group(2).lstrip().startswith("![")
        or m_w.group(2).lstrip().lower().startswith("<img")
    ):
        return line, False

    spans = _merge_spans(_md_image_spans(body) + _html_img_spans(body))
    if not spans:
        return line, False

    parts: list[str] = []
    cur = 0
    for a, b in spans:
        parts.append(body[cur:a])
        parts.append(_wrap_in_comment(body[a:b]))
        cur = b
    parts.append(body[cur:])
    return "".join(parts) + eol, True


def _inner_is_image(inner: str) -> bool:
    t = inner.strip()
    if t.startswith("!["):
        return True
    if t.lstrip()[:1] == "<" and re.match(r"(?is)^\s*<img\b", t):
        return True
    return False


def uncomment_line(line: str) -> tuple[str, bool]:
    """Remove one level of our HTML image comments on the line where applicable."""
    raw = line
    eol = ""
    if raw.endswith("\r\n"):
        body, eol = raw[:-2], "\r\n"
    elif raw.endswith("\n"):
        body, eol = raw[:-1], "\n"
    else:
        body, eol = raw, ""

    m = _WHOLE_COMMENT.match(body)
    if m and _inner_is_image(m.group(2)):
        return m.group(1) + m.group(2).rstrip() + m.group(3) + eol, True

    if "<!--" not in body or "-->" not in body:
        return line, False

    out = []
    i = 0
    changed = False
    while i < len(body):
        a = body.find("<!--", i)
        if a < 0:
            out.append(body[i:])
            break
        out.append(body[i:a])
        b = body.find("-->", a + 4)
        if b < 0:
            out.append(body[a:])
            break
        inner = body[a + 4 : b]
        if _inner_is_image(inner):
            out.append(inner.strip())
            changed = True
        else:
            out.append(body[a : b + 3])
        i = b + 3
    if not changed:
        return line, False
    return "".join(out) + eol, True


def transform_file_text(text: str, mode: str) -> tuple[str, bool]:
    in_fence = False
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if mode == "comment":
            nxt, _ = comment_out_line(line)
        else:
            nxt, _ = uncomment_line(line)
        out.append(nxt)
    joined = "".join(out)
    return joined, joined != text


def process_file(path: Path, mode: str) -> bool:
    data = path.read_text(encoding="utf-8")
    new, _ = transform_file_text(data, mode)
    if new != data:
        path.write_text(new, encoding="utf-8", newline="")
        return True
    return False


def _relpath_display(path: Path, base: Path) -> str:
    try:
        return str(path.resolve().relative_to(base.resolve()))
    except ValueError:
        return str(path)


def _line_change_stats(
    data: str, new: str
) -> tuple[int, int]:
    """(lines with different content, size delta in bytes)."""
    a = data.splitlines(keepends=True)
    b = new.splitlines(keepends=True)
    if len(a) == len(b):
        diff_lines = sum(1 for i in range(len(a)) if a[i] != b[i])
    else:
        diff_lines = 0
        m = min(len(a), len(b))
        for i in range(m):
            if a[i] != b[i]:
                diff_lines += 1
        diff_lines += abs(len(a) - len(b))
    return (diff_lines, len(new) - len(data))


def _count_fenced_and_images(data: str) -> tuple[int, int, int]:
    """(lines inside ``` fences, rough count of '![', rough count of '<img')."""
    in_f = False
    fenced = 0
    img_markers = 0
    open_tags = 0
    for line in data.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            in_f = not in_f
        if in_f:
            fenced += 1
            continue
        s = line
        img_markers += s.count("![")
        if re.search(r"<\s*img\s", s, re.I):
            open_tags += 1
    return (fenced, img_markers, open_tags)


def _is_under_cwd(p: Path, cwd: Path) -> bool:
    try:
        p.resolve().relative_to(cwd.resolve())
        return True
    except ValueError:
        return False


def _print_header(
    *,
    mode: str,
    root: Path,
    n_files: int,
    dry: bool,
    quiet: bool,
) -> None:
    if quiet:
        return
    tag = " (dry run - no writes)" if dry else ""
    print(f"comment_out_image_links{tag}", file=sys.stdout)
    if mode == "comment":
        print("  Mode: comment - wrap ![]() and <img> in <!-- ... -->", file=sys.stdout)
    else:
        print("  Mode: uncomment - remove those <!-- ... --> image wrappers", file=sys.stdout)
    res = root.resolve()
    cwd = Path.cwd().resolve()
    res_rel = res.relative_to(cwd) if _is_under_cwd(res, cwd) else res
    print(f"  Root (absolute): {res}", file=sys.stdout)
    print(f"  Root (from cwd): {res_rel}", file=sys.stdout)
    print(f"  Working directory: {os.getcwd()}", file=sys.stdout)
    print(
        f"  Markdown files: {n_files} (recursive rglob * under root).", file=sys.stdout
    )
    print(file=sys.stdout)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Comment out or restore image links in .md (HTML comment wrappers).",
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path("help/painting/generators"),
        help="Root directory to search for *.md (default: help/painting/generators)",
    )
    parser.add_argument(
        "--uncomment",
        action="store_true",
        help="Remove our HTML comment wrappers and restore image markup.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change, without writing.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print a one-line summary (and errors).",
    )
    args = parser.parse_args()
    root: Path = args.path
    if not root.is_dir():
        print(f"Not a directory: {root.resolve()}", file=sys.stderr)
        print(
            "  Fix the path, or run from the repo root so the default help/painting/... exists.",
            file=sys.stderr,
        )
        return 1
    mode: str = "uncomment" if args.uncomment else "comment"
    dry = args.dry_run
    quiet = args.quiet
    base = root.resolve()
    md_files = sorted(root.rglob("*.md"))
    n_total = len(md_files)

    _print_header(
        mode=mode,
        root=root,
        n_files=n_total,
        dry=dry,
        quiet=quiet,
    )
    to_touch: list[Path] = []
    n_lines_total = 0
    n_bytes_total = 0
    for f in md_files:
        data = f.read_text(encoding="utf-8")
        new, _ = transform_file_text(data, mode)
        rel = _relpath_display(f, base)
        if new != data:
            to_touch.append(f)
            dl, dbytes = _line_change_stats(data, new)
            n_lines_total += dl
            n_bytes_total += dbytes
            if not quiet:
                if dry:
                    print(
                        f"  WOULD change: {rel}  - {dl} line(s) differ, {dbytes:+d} bytes",
                        file=sys.stdout,
                    )
                else:
                    print(
                        f"  will write:  {rel}  - {dl} line(s) would change, {dbytes:+d} bytes",
                        file=sys.stdout,
                    )
        else:
            _fenc_lines, n_bang, n_tag = _count_fenced_and_images(data)
            if not quiet:
                if n_bang or n_tag:
                    reason = (
                        f"heuristic: {n_bang} `![' in unfenced text, {n_tag} <img> line(s); "
                        f"transform is already a no-op for this mode"
                    )
                else:
                    reason = "no `![' in unfenced text (or only in ``` blocks); nothing to transform"
                print(
                    f"  unchanged:  {rel}  - {reason}.",
                    file=sys.stdout,
                )

    if n_total == 0 and not quiet:
        print("  (No .md files found. Check the root path.)", file=sys.stdout)
    if not quiet:
        print(file=sys.stdout)
        if dry:
            print(
                f"Summary: would change {len(to_touch)} of {n_total} file(s) "
                f"({n_lines_total} line diff total, {n_bytes_total:+d} bytes), mode={mode}.",
                file=sys.stdout,
            )
            if len(to_touch) == 0 and n_total > 0:
                print(
                    "  Nothing to do: every file already matches the result of this mode. "
                    "In comment mode, that usually means images are already in <!-- -->.",
                    file=sys.stdout,
                )
                print(
                    "  Try:  python ... --uncomment   to unwrap, then run comment again to test.",
                    file=sys.stdout,
                )
        else:
            print(
                f"Summary: {len(to_touch)} of {n_total} file(s) to write, "
                f"{n_lines_total} line diffs, {n_bytes_total:+d} bytes, mode={mode}.",
                file=sys.stdout,
            )

    changed: list[Path] = []
    if not dry:
        if not quiet and len(to_touch) > 0:
            print("Writing to disk...", file=sys.stdout)
        for f in md_files:
            if process_file(f, mode):
                changed.append(f)
        if not quiet and len(changed) > 0:
            print(
                f"Done. Wrote {len(changed)} file(s) (mode={mode}).",
                file=sys.stdout,
            )
    if not dry and quiet:
        print(
            f"comment_out_image_links: {len(changed)}/{n_total} file(s) written (mode={mode}).",
            file=sys.stdout,
        )
    if not dry and not quiet and len(changed) == 0 and n_total > 0 and len(to_touch) == 0:
        print(file=sys.stdout)
        print(
            "No files were written. See 'unchanged' lines above, or the summary. "
            "In comment mode: images are probably already in <!-- -->. In uncomment: no matching wrappers found.",
            file=sys.stdout,
        )
    if not dry and not quiet and len(changed) != len(to_touch):
        print(
            f"Internal note: to_touch={len(to_touch)} vs wrote={len(changed)} (should match).",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())