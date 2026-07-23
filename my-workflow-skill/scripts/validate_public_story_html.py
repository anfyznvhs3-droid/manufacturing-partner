#!/usr/bin/env python3
"""Validate the public-facing manufacturing explainer HTML contract."""

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class StoryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids = set()
        self.demo_states = set()
        self.attributes = set()
        self.text_parts = []
        self.external_resources = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get("id"):
            self.ids.add(attrs_dict["id"])
        if attrs_dict.get("data-demo"):
            self.demo_states.add(attrs_dict["data-demo"])
        self.attributes.update(attrs_dict)
        for key in ("src", "href"):
            value = attrs_dict.get(key, "")
            if value.startswith(("http://", "https://", "//")):
                self.external_resources.append(value)

    def handle_data(self, data):
        self.text_parts.append(data)


def validate(html_path: Path, contract_path: Path) -> dict:
    if not html_path.exists():
        return {"valid": False, "errors": [f"missing-html:{html_path}"]}
    parser = StoryParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    body = " ".join(parser.text_parts)
    compact_body = re.sub(r"\s+", "", body)
    errors = []
    errors.extend(f"missing-id:{item}" for item in contract["required_ids"] if item not in parser.ids)
    errors.extend(f"missing-text:{item}" for item in contract["required_text"] if re.sub(r"\s+", "", item) not in compact_body)
    errors.extend(f"missing-demo-state:{item}" for item in contract["required_demo_states"] if item not in parser.demo_states)
    errors.extend(f"missing-attribute:{item}" for item in contract["required_attributes"] if item not in parser.attributes)
    errors.extend(f"forbidden-text:{item}" for item in contract["forbidden_text"] if item.lower() in body.lower())
    errors.extend(f"external-resource:{item}" for item in parser.external_resources)
    return {
        "valid": not errors,
        "errors": errors,
        "section_count": len(parser.ids),
        "demo_state_count": len(parser.demo_states),
        "external_resource_count": len(parser.external_resources),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = validate(args.input, args.contract)
    if args.report:
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
