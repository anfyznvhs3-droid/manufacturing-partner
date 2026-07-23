#!/usr/bin/env python3
"""Extract PDF text once and report a reproducible cl100k_base token baseline."""

import argparse
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader
import tiktoken


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--text-output", required=True, type=Path)
    parser.add_argument("--report-output", required=True, type=Path)
    parser.add_argument("--comparison-input", type=Path,
                        help="Optional compact fact pack to measure against the full PDF text.")
    args = parser.parse_args()

    reader = PdfReader(args.input)
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n\n".join(f"--- page {index + 1} ---\n{page}" for index, page in enumerate(pages))
    encoding = tiktoken.get_encoding("cl100k_base")
    args.text_output.write_text(text, encoding="utf-8")
    report = {
        "input": args.input.name,
        "sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "pages": len(pages),
        "characters": len(text),
        "nonempty_pages": sum(bool(page.strip()) for page in pages),
        "tokenizer": "cl100k_base",
        "estimated_tokens": len(encoding.encode(text)),
        "note": "Tokenizer baseline for comparison only; production model token counts can differ.",
    }
    if args.comparison_input:
        comparison_text = args.comparison_input.read_text(encoding="utf-8")
        comparison_tokens = len(encoding.encode(comparison_text))
        report["comparison_input"] = args.comparison_input.name
        report["comparison_tokens"] = comparison_tokens
        report["comparison_reduction_percent"] = round(
            (1 - comparison_tokens / report["estimated_tokens"]) * 100, 1
        )
    args.report_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
