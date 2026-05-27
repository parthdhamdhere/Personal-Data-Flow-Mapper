import sys
import argparse
from mapper.scanner import scan_directory, scan_file
from mapper.reporter import print_report


def main():
    parser = argparse.ArgumentParser(
        description="Personal Data Flow Mapper — static analysis for privacy"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="sample_app",
        help="File or directory to scan (default: sample_app)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output findings as JSON"
    )
    args = parser.parse_args()

    import os
    if os.path.isfile(args.target):
        findings = scan_file(args.target)
    elif os.path.isdir(args.target):
        findings = scan_directory(args.target)
    else:
        print(f"Error: '{args.target}' is not a valid file or directory.")
        sys.exit(1)

    print_report(findings, use_json=args.json)


if __name__ == "__main__":
    main()
