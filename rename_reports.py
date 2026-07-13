#!/usr/bin/env python3
"""
Rename InvestingPro "Pro Research" PDFs from their encoded download names
to clean TICKER_ProResearch.pdf names.

Usage:
    cd /Users/artemsychov/projects/ai_augmented_investing
    python3 rename_reports.py           # dry run: shows what would happen
    python3 rename_reports.py --apply    # actually renames

The mapping keys are the leading characters of each downloaded filename
(the base64 string before ".pdf"). The script matches any file in the
folder whose name starts with that prefix, so you don't need the full
encoded string.
"""

import sys
from pathlib import Path

FOLDER = Path("/Users/artemsychov/projects/ai_augmented_investing/jul_12_research/")

# prefix of the downloaded (encoded) filename  ->  ticker
MAPPING = {
    "MTMyMzgz": "LULU",   # Lululemon Athletica
    "MTE1NzIy": "CHTR",   # Charter Communications
    "MTMyMzQx": "EPAM",   # EPAM Systems
    "MTM5MTM1": "IT",     # Gartner
    "MTc4ODR":  "ACN",    # Accenture
    "MTYzNzB":  "FI",     # Fiserv
    "MTYzNzN":  "ADBE",   # Adobe
    "MTY0NTR":  "CTSH",   # Cognizant
    "MTgwNDJ":  "FIS",    # Fidelity National Information Services
    "MTY0NDh":  "INTU",   # Intuit
    "MTE2NjMx": "MKTX",   # MarketAxess
    "MTMyMzYx": "WDAY",   # Workday
    "MTY1MTZ":  "CMCSA",  # Comcast
    "MTc4ODl":  "CI",     # Cigna
    "MTgyOTR":  "CRM",    # Salesforce
    "MTM5MTQ3": "UHS",    # Universal Health Services
    "MTI0MzEy": "TYL",    # Tyler Technologies
    "MTE5Njk2": "LDOS",   # Leidos Holdings
    "MTEzODYz": "ROP",    # Roper Technologies
    "MTgyNDh":  "BSX",    # Boston Scientific
    "MTIwMzIy": "FDS",    # FactSet
    "MTM5MTU5": "BR",     # Broadridge
    "MTYzNjN":  "ADSK",   # Autodesk
    "MTMyNTI0": "ALB",    # Albemarle
    "MTE2OTMy": "PTC",    # PTC
    "MTM5MTUy": "LKQ",    # LKQ
    "MTE2OTQz": "POOL",   # Pool Corp
    "MTMyMzkx": "REGN",   # Regeneron
    "MTE1ODI4": "CSGP",   # CoStar Group
    "MTgxNTB":  "NEM",    # Newmont
}

# Order prefixes longest-first so more-specific ones win over shorter overlaps.
PREFIXES = sorted(MAPPING.items(), key=lambda kv: len(kv[0]), reverse=True)


def main():
    apply = "--apply" in sys.argv

    if not FOLDER.exists():
        print(f"Folder not found: {FOLDER}")
        sys.exit(1)

    pdfs = sorted(FOLDER.glob("*.pdf"))
    if not pdfs:
        print(f"No .pdf files found in {FOLDER}")
        sys.exit(1)

    used = {}          # ticker -> count, to handle any duplicates safely
    matched, unmatched = [], []

    for pdf in pdfs:
        ticker = None
        for prefix, tk in PREFIXES:
            if pdf.name.startswith(prefix):
                ticker = tk
                break
        if ticker is None:
            unmatched.append(pdf)
            continue

        used[ticker] = used.get(ticker, 0) + 1
        suffix = "" if used[ticker] == 1 else f"_{used[ticker]}"
        new_name = f"{ticker}_ProResearch{suffix}.pdf"
        matched.append((pdf, FOLDER / new_name))

    print(f"{'APPLYING' if apply else 'DRY RUN'} — {len(matched)} file(s) to rename\n")
    for old, new in matched:
        print(f"  {old.name}\n    -> {new.name}")
        if apply:
            if new.exists() and new != old:
                print(f"    !! target already exists, skipping")
                continue
            old.rename(new)

    if unmatched:
        print(f"\n{len(unmatched)} file(s) did NOT match any known prefix:")
        for u in unmatched:
            print(f"  {u.name}")

    print(f"\nMatched {len(matched)} / {len(pdfs)} PDFs.")
    if not apply:
        print("\nThis was a dry run. Re-run with --apply to perform the renames:")
        print("    python3 rename_reports.py --apply")


if __name__ == "__main__":
    main()
