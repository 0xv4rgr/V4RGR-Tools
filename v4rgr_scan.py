#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

from modules.username import run_username_scan


def build_markdown_report(target_type: str, value: str, results: dict) -> str:
    """Builds a markdown report and saves it under reports/."""
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    ts = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"report-{target_type}-{value}-{ts}.md".replace("/", "_")
    path = reports_dir / filename

    lines = []
    lines.append(f"# 🔥 V4RGR ONE-SCAN Report")
    lines.append("")
    lines.append(f"**Target Type:** `{target_type}`")
    lines.append(f"**Target Value:** `{value}`")
    lines.append(f"**Generated (UTC):** {ts}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for section, content in results.items():
        lines.append(f"## {section}")
        lines.append("")
        if isinstance(content, list):
            for item in content:
                lines.append(f"- {item}")
        else:
            lines.append("```")
            lines.append(str(content))
            lines.append("```")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)


def main():
    parser = argparse.ArgumentParser(
        description="V4RGR ONE-SCAN — multi-target OSINT scanner."
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=["username"],
        help="Target type to scan",
    )
    parser.add_argument(
        "--value",
        required=True,
        help="Target value (username/email/domain etc.)",
    )

    args = parser.parse_args()

    results = {}

    if args.type == "username":
        results["Username OSINT Results"] = run_username_scan(args.value)

    report_path = build_markdown_report(args.type, args.value, results)
    print(f"[+] Scan complete. Report saved at: {report_path}")


if __name__ == "__main__":
    main()
