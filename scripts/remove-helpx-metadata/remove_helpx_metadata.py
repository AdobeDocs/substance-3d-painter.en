#!/usr/bin/env python3
"""Remove helpx-prefixed fields from Markdown YAML front matter."""

import argparse
import re
import sys
from pathlib import Path


_BOM = b"\xef\xbb\xbf"
_FIELD = re.compile(
    rb"""^(?:helpx[^ \t:'"]*|'helpx[^']*'|"helpx[^"]*")[ \t]*:(?:[ \t]|$)"""
)
_KEY = re.compile(
    rb"""^(?![-?][ \t])(?:[^ \t#:'"][^:]*|'[^']*'|"[^"]*")[ \t]*:(?:[ \t]|$)"""
)


def remove_helpx_metadata(content: bytes) -> tuple[bytes, int]:
    """Return edited bytes and field count, preserving all unrelated bytes."""
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].removeprefix(_BOM).rstrip(b" \t\r\n") != b"---":
        return content, 0

    end = next(
        (
            i
            for i in range(1, len(lines))
            if lines[i].rstrip(b" \t\r\n") in (b"---", b"...")
        ),
        None,
    )
    if end is None:
        raise ValueError("YAML front matter has no closing delimiter")

    result = [lines[0]]
    removing = False
    count = 0
    for line in lines[1:end]:
        if _KEY.match(line):
            removing = bool(_FIELD.match(line))
            count += int(removing)
        if not removing or not line.strip() or line.lstrip().startswith(b"#"):
            result.append(line)
    result.extend(lines[end:])
    return b"".join(result), count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode", type=int, choices=(1, 2), help="1: dry run; 2: remove fields"
    )
    parser.add_argument(
        "path", nargs="?", type=Path, default=Path.cwd(), help="folder (default: current folder)"
    )
    args = parser.parse_args(argv)
    if not args.path.is_dir():
        parser.error(f"not a directory: {args.path}")

    scanned = affected = instances = errors = 0
    try:
        for path in args.path.rglob("*"):
            if not path.is_file() or path.suffix.lower() != ".md":
                continue
            scanned += 1
            try:
                original = path.read_bytes()
                updated, count = remove_helpx_metadata(original)
                if count:
                    if args.mode == 2:
                        path.write_bytes(updated)
                    affected += 1
                    instances += count
                    action = "Found" if args.mode == 1 else "Removed"
                    print(f"{action} {count} instance(s): {path}")
            except (OSError, ValueError) as exc:
                print(f"Error: {path}: {exc}", file=sys.stderr)
                errors += 1
    except OSError as exc:
        print(f"Error scanning {args.path}: {exc}", file=sys.stderr)
        errors += 1

    label = "Dry run" if args.mode == 1 else "Removal"
    print(
        f"{label}: {scanned} Markdown file(s) scanned; "
        f"{affected} file(s) with {instances} instance(s)"
        f"{' found' if args.mode == 1 else ' removed'}; {errors} error(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
