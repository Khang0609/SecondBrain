#!/usr/bin/env python3
"""Preprocess difficult source formats (YouTube, DOCX, PPTX, XLSX) into Gemini-ready files.

Outputs:
- YouTube URLs -> .srt subtitles (or 480p .mp4 with --download-video) in raw/youtube/
- Office files (.docx, .pptx, .xlsx) -> extracted Markdown in raw/.extracted/
- Other formats (.pdf, images, video, audio, .md) -> read directly via multimodal tools
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from markitdown import MarkItDown

# Ensure UTF-8 console output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

OUT_DIR = Path("raw/.extracted")
YT_DIR = Path("raw/youtube")
OFFICE_EXTENSIONS = {".docx", ".pptx", ".xlsx"}


def is_youtube_url(target: str) -> bool:
    return target.startswith(("http://", "https://")) and (
        "youtube.com" in target or "youtu.be" in target
    )


def handle_youtube(url: str) -> None:
    """Download Vietnamese or English subtitles (.srt) into raw/youtube/."""
    YT_DIR.mkdir(parents=True, exist_ok=True)
    cmd_sub = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--skip-download",
        "--write-auto-sub",
        "--write-sub",
        "--sub-lang",
        "vi,en",
        "--convert-subs",
        "srt",
        "-o",
        str(YT_DIR / "%(title)s [%(id)s].%(ext)s"),
        url,
    ]
    subprocess.run(cmd_sub, check=False)
    print(
        f"YOUTUBE_PROCESSED: Check the latest .srt file in {YT_DIR}. "
        "If the video has no subtitles or relies heavily on visuals/slides, "
        "re-run with --download-video."
    )


def handle_youtube_video(url: str) -> None:
    """Download 480p .mp4 video into raw/youtube/ for direct multimodal analysis."""
    YT_DIR.mkdir(parents=True, exist_ok=True)
    cmd_vid = [
        sys.executable,
        "-m",
        "yt_dlp",
        "-f",
        "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]",
        "-o",
        str(YT_DIR / "%(title)s [%(id)s].%(ext)s"),
        url,
    ]
    subprocess.run(cmd_vid, check=True)
    print(
        f"YOUTUBE_VIDEO_DOWNLOADED: Saved .mp4 to {YT_DIR}. "
        "Read this video file directly."
    )


def handle_office(file_path: Path) -> None:
    """Convert .docx, .pptx, or .xlsx to Markdown in raw/.extracted/ without modifying raw/."""
    if not file_path.is_file():
        raise FileNotFoundError(f"Source file not found: {file_path}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    md = MarkItDown()
    result = md.convert(str(file_path))
    out_file = OUT_DIR / f"{file_path.stem}.md"
    out_file.write_text(result.text_content, encoding="utf-8")
    print(f"OFFICE_EXTRACTED: Extracted content to {out_file}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Preprocess YouTube URLs and Office documents (.docx, .pptx, .xlsx) for /wiki-ingest."
    )
    parser.add_argument("target", help="Path to a file in raw/ or a YouTube URL.")
    parser.add_argument(
        "--download-video",
        action="store_true",
        help="Download 480p .mp4 video for YouTube URLs when subtitles are missing or visuals matter.",
    )
    args = parser.parse_args(argv)

    if is_youtube_url(args.target):
        if args.download_video:
            handle_youtube_video(args.target)
        else:
            handle_youtube(args.target)
        return 0

    path = Path(args.target)
    if path.suffix.lower() in OFFICE_EXTENSIONS:
        handle_office(path)
    else:
        print(
            f"DIRECT_MULTIMODAL: Antigravity can read {path} directly without conversion."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
