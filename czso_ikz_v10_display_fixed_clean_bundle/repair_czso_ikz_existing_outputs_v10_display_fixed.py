from __future__ import annotations
import argparse
from pathlib import Path
from czso_ikz_v10_robust_patch import repair_existing_output

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Repair/reorder an existing CZSO IKZ v10 output directory in place.")
    p.add_argument("--output-dir", required=True)
    p.add_argument("--target-years", nargs="+", type=int, default=[2023, 2024])
    p.add_argument("--force-redownload", action="store_true")
    p.add_argument("--keep-downloads", action="store_true")
    p.add_argument("--pause-seconds", type=float, default=0.0)
    return p

def main() -> int:
    args = build_parser().parse_args()
    repair_existing_output(
        Path(args.output_dir),
        refresh_recent_single_year=True,
        target_years=args.target_years,
        force_redownload=bool(args.force_redownload),
        pause_seconds=float(args.pause_seconds),
        cleanup_downloaded_files=not bool(args.keep_downloads),
        persist=True,
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
