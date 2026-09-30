from __future__ import annotations

import argparse
import os
import sys

from autofill_preset import default_preset_path
from sbs_dump_config import SBSDumpConfig
from sbs_param_gui import collect_sbs_paths, run_export


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Batch-export Markdown parameter docs from SBS files."
    )
    parser.add_argument("source", help="Path to an .sbs file or a folder containing .sbs files.")
    parser.add_argument("output", help="Directory where generated files should be written.")
    parser.add_argument(
        "--preset",
        default=default_preset_path(),
        help="Path to the autofill preset JSON. Defaults to the bundled designer preset.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recursively scan the source folder for .sbs files.",
    )
    parser.add_argument(
        "--config-mode",
        choices=("folder-library", "default"),
        default="folder-library",
        help="Export config preset. 'folder-library' matches the legacy folder-based library layout.",
    )
    return parser


def resolve_config(mode: str) -> SBSDumpConfig:
    if mode == "default":
        return SBSDumpConfig()
    return SBSDumpConfig.folder_library_style()


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    source = os.path.abspath(args.source)
    output = os.path.abspath(args.output)
    paths = collect_sbs_paths(source, recursive=args.recursive)
    if not paths:
        parser.error(f"No .sbs files found at: {source}")

    os.makedirs(output, exist_ok=True)
    config = resolve_config(args.config_mode)

    def log(message: str) -> None:
        print(message)

    ok, err, artifacts = run_export(
        paths=paths,
        out_dir=output,
        config=config,
        write_html=False,
        write_md=True,
        autofill_path=os.path.abspath(args.preset),
        log=log,
    )
    print(f"Finished: {ok} ok, {err} failed or skipped.")
    print(f"Output: {artifacts['out_dir']}")
    return 0 if ok > 0 and err == 0 else 1 if ok == 0 else 0


if __name__ == "__main__":
    sys.exit(main())