#!/usr/bin/env python3
"""Entry point for the news-image-20261125 make.fun bounty.

Copies the pre-drawn news.png (sitting beside this file) to
$MAKEFUN_OUTPUT_DIR/entry.png. Standard library only: the grader
sandbox has no PIL and no fonts, so nothing is drawn at runtime.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "news.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
