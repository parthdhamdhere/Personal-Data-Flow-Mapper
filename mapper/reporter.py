import json


def print_report(findings, use_json=False):
    if use_json:
        print(json.dumps(findings, indent=2))
        return

    if not findings:
        print("\n✅ No personal data flows detected.\n")
        return

    sources = [f for f in findings if f["type"] == "SOURCE"]
    sinks   = [f for f in findings if f["type"] == "SINK"]

    risk_level = "HIGH" if sinks else "LOW"
    risk_icon  = "🔴" if risk_level == "HIGH" else "🟡"

    print("\n" + "=" * 60)
    print("  PERSONAL DATA FLOW MAPPER — SCAN REPORT")
    print("=" * 60)
    print(f"  Total Findings : {len(findings)}")
    print(f"  Sources Found  : {len(sources)}")
    print(f"  Sinks Found    : {len(sinks)}")
    print(f"  Risk Level     : {risk_icon}  {risk_level}")
    print("=" * 60)

    if sources:
        print("\n📌 SOURCES  (personal data assigned)")
        print("-" * 60)
        for f in sources:
            print(f"  [{f['risk']}] {f['file']}  line {f['line']}")
            print(f"         Variable: {f['variable']}")

    if sinks:
        print("\n🚨 SINKS  (personal data leaving the system)")
        print("-" * 60)
        for f in sinks:
            print(f"  [{f['risk']}] {f['file']}  line {f['line']}")
            print(f"         Variable : {f['variable']}")
            print(f"         Sink     : {f['sink']}")
            print(f"         Code     : {f['code'][:80]}")

    print("\n" + "=" * 60 + "\n")
