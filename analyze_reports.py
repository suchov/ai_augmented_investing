#!/usr/bin/env python3
"""
Step 2 — AI Analyst (Claude CLI edition)
========================================
Reads each Pro Research PDF in the project folder and analyzes it by calling
your LOCAL `claude` command-line tool (Claude Code) in non-interactive mode.
No API key, no per-token API billing — it uses whatever Claude subscription
your `claude` CLI is already logged into.

REQUIREMENTS:
    - Claude Code CLI installed and logged in. Check with:  claude --version
      (If missing, install per https://code.claude.com and run `claude` once
       to log in.)
    - pypdf for text extraction:  pip install pypdf

USAGE:
    cd /Users/artemsychov/projects/ai_augmented_investing
    python analyze_reports_cli.py                # analyze every *_ProResearch.pdf
    python analyze_reports_cli.py LULU CHTR       # only specific tickers
    python analyze_reports_cli.py --overwrite     # redo even if analysis exists
    python analyze_reports_cli.py --model sonnet  # pick a model (default: opus)

Outputs -> ./analysis/<TICKER>_analysis.md

HOW IT WORKS:
    For each PDF it extracts the text locally, then runs:
        claude -p --bare --model <model> --append-system-prompt "<brief>" < <report text>
    The report text is piped in on stdin; Claude Code appends it to the prompt,
    runs once, prints the analysis to stdout, and exits.
"""

import argparse
import subprocess
import sys
from pathlib import Path

FOLDER = Path("/Users/artemsychov/projects/ai_augmented_investing/jul_12_research/")
OUT_DIR = FOLDER / "analysis"
DEFAULT_MODEL = "opus"          # opus | sonnet | haiku — sonnet/haiku are cheaper/faster
STDIN_CAP_BYTES = 9_500_000     # stay under Claude Code's ~10MB piped-stdin cap

SYSTEM_PROMPT = """You are a disciplined value-investing analyst in the tradition of Warren Buffett and Peter Lynch. You are given the text of an InvestingPro "Pro Research" report for a single company (it follows this message on stdin). Analyze ONLY what the report supports; where it lacks data for a question, write "Not covered in report" rather than inventing figures. Be concise and specific, cite numbers from the report where available, and keep a skeptical, owner-minded tone. Do not use any tools or read any files; just analyze the text you are given and print the result.

Output Markdown with exactly these sections:

## Business
- How does the company earn money?
- Does it have a moat? What kind (switching costs, network effects, brand, regulatory, cost advantage, data)?
- Who are the main competitors?

## Financials
- Revenue CAGR, EPS CAGR, FCF CAGR (state the period if given)
- ROIC / returns on capital
- Debt level and balance-sheet health

## Risks
- Regulatory exposure
- AI / technological disruption
- Customer or supplier concentration
- Any other red flags the report raises

## Valuation
- The report's fair-value estimate and implied upside/downside
- Whether the current price looks cheap, fair, or rich given the fundamentals
- What the market may be missing (bull) and what could go wrong (bear)

## Verdict
One paragraph: would a patient value investor want to dig deeper here? What is the single most important thing to verify next?"""


def check_cli():
    try:
        r = subprocess.run(["claude", "--version"],
                           capture_output=True, text=True, timeout=30)
        if r.returncode == 0:
            print(f"Using claude CLI: {r.stdout.strip()}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    print("ERROR: `claude` CLI not found or not responding.")
    print("Install Claude Code and log in (run `claude` once interactively), then retry.")
    return False


def extract_pdf_text(path):
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    parts = [p.extract_text() or "" for p in reader.pages]
    text = "\n\n".join(t for t in parts if t.strip()).strip()
    if len(text.encode("utf-8")) > STDIN_CAP_BYTES:
        text = text.encode("utf-8")[:STDIN_CAP_BYTES].decode("utf-8", "ignore")
    return text


def find_pdfs(only_tickers):
    pdfs = {}
    for p in sorted(FOLDER.glob("*_ProResearch*.pdf")):
        ticker = p.name.split("_")[0].upper()
        pdfs.setdefault(ticker, p)
    if only_tickers:
        want = {t.upper() for t in only_tickers}
        pdfs = {t: p for t, p in pdfs.items() if t in want}
    return pdfs


def analyze(text, ticker, model):
    """Run claude -p once, piping the report text on stdin. Returns analysis str."""
    prompt = (f"Analyze the Pro Research report for ticker {ticker}. "
              f"The full report text follows on stdin. Produce the structured analysis.")
    cmd = [
        "claude", "-p", prompt,
        "--model", model,
        "--append-system-prompt", SYSTEM_PROMPT,
        "--max-turns", "1",                     # one shot; no tool loop
    ]
    r = subprocess.run(cmd, input=text, capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip() or f"claude exited with code {r.returncode}")
    return r.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tickers", nargs="*", help="Optional list of tickers to limit to")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    args = ap.parse_args()

    if not FOLDER.exists():
        print(f"Folder not found: {FOLDER}")
        sys.exit(1)
    if not check_cli():
        sys.exit(1)
    try:
        import pypdf  # noqa: F401
    except ImportError:
        print("ERROR: install pypdf first:  pip install pypdf")
        sys.exit(1)

    pdfs = find_pdfs(args.tickers)
    if not pdfs:
        print("No matching *_ProResearch.pdf files found. "
              "Run the rename script first, or check the ticker names.")
        sys.exit(1)

    OUT_DIR.mkdir(exist_ok=True)
    print(f"Analyzing {len(pdfs)} report(s) with model '{args.model}'\n")
    done, skipped, failed = 0, 0, 0

    for ticker, pdf in pdfs.items():
        out_path = OUT_DIR / f"{ticker}_analysis.md"
        if out_path.exists() and not args.overwrite:
            print(f"  [skip] {ticker} — analysis exists (use --overwrite to redo)")
            skipped += 1
            continue

        print(f"  [{ticker}] extracting...", end=" ", flush=True)
        try:
            text = extract_pdf_text(pdf)
        except Exception as e:
            print(f"FAILED to read PDF: {e}")
            failed += 1
            continue
        if len(text) < 200:
            print("(little text extracted — PDF may be image-only)", end=" ")

        print("analyzing...", end=" ", flush=True)
        try:
            analysis = analyze(text, ticker, args.model)
        except Exception as e:
            print(f"FAILED: {e}")
            failed += 1
            continue

        header = f"# {ticker} — AI Analyst Summary\n\n*Source: {pdf.name} · via claude CLI ({args.model})*\n\n---\n\n"
        out_path.write_text(header + analysis, encoding="utf-8")
        print(f"saved -> analysis/{out_path.name}")
        done += 1

    print(f"\nDone. {done} analyzed, {skipped} skipped, {failed} failed.")
    if done:
        print(f"Output folder: {OUT_DIR}")


if __name__ == "__main__":
    main()
