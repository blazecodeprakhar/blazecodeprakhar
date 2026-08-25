#!/usr/bin/env python3
"""
update.py — One-shot contribution graph refresher
===================================================
Run this file from inside the repo:

    python update.py

What it does (in order):
  1. Fetches the latest contribution data from GitHub (scripts/fetch_contributions.py)
  2. Re-renders the animated heatmap SVG        (scripts/render_heatmap_svg.py)
  3. Re-renders the streak SVG                  (scripts/generate_streak_svg.py)
  4. Stages every changed/new file              (git add -A)
  5. Commits with the standard auto-commit msg  "chore: refresh contribution graph [skip ci]"
  6. Pushes to origin/main (or origin/master)

No manual git steps needed — just run this file and walk away.
"""

import datetime
import os
import subprocess
import sys

# ── repo root is the directory that contains this file ──────────────────────
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS   = os.path.join(REPO_ROOT, "scripts")

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

COMMIT_MSG = "chore: refresh contribution graph [skip ci]"

# ── helpers ─────────────────────────────────────────────────────────────────

def banner(text: str) -> None:
    width = 60
    print()
    print("=" * width)
    print(f"  {text}")
    print("=" * width)


def run(cmd: list, cwd: str = REPO_ROOT, check: bool = True) -> subprocess.CompletedProcess:
    """Run a command, stream its output, and (optionally) raise on failure."""
    print(f"\n>  {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        capture_output=False,
    )
    if check and result.returncode != 0:
        print(f"\n[X] Command failed with exit code {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)
    return result


def py(script_name: str, *args: str) -> None:
    """Run a Python script from the scripts/ directory."""
    script_path = os.path.join(SCRIPTS, script_name)
    run([sys.executable, script_path, *args])


# ── main pipeline ────────────────────────────────────────────────────────────

def main() -> None:
    start = datetime.datetime.now()
    banner(f"Refreshing contribution graph  —  {start.strftime('%Y-%m-%d %H:%M:%S')}")

    # Step 1: fetch fresh contribution data
    banner("Step 1 / 3  |  Fetching contribution data from GitHub")
    py("fetch_contributions.py")

    # Step 2: regenerate the heatmap SVG
    banner("Step 2 / 3  |  Rendering animated heatmap SVG")
    py("render_heatmap_svg.py")

    # Step 3: regenerate the streak SVG
    banner("Step 3 / 3  |  Generating streak SVG")
    streak_out = os.path.join(REPO_ROOT, "streak.svg")
    py("generate_streak_svg.py", "blazecodeprakhar", streak_out)

    # git add -> commit -> push
    banner("Git  |  Staging, committing, and pushing")

    run(["git", "add", "-A"])

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if not status.stdout.strip():
        print("\nNothing changed since last run — repo is already up to date.")
    else:
        print("\nChanged files:")
        print(status.stdout)

        run(["git", "commit", "-m", COMMIT_MSG])

        push_result = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=REPO_ROOT,
            text=True,
        )
        if push_result.returncode != 0:
            print("  'main' branch not found, trying 'master' ...")
            run(["git", "push", "origin", "master"])

        print("\nSuccessfully pushed to GitHub!")

    elapsed = (datetime.datetime.now() - start).total_seconds()
    banner(f"Done in {elapsed:.1f}s  — contribution graph is live on GitHub!")


if __name__ == "__main__":
    main()
