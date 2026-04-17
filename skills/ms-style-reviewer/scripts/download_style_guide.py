from __future__ import annotations

from style_guide_downloader import build_arg_parser, run_download


def main() -> int:
    parser = build_arg_parser(default_output_dir="web")
    args = parser.parse_args()
    return run_download(args)


if __name__ == "__main__":
    raise SystemExit(main())