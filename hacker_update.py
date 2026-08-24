#!/usr/bin/env python3
"""
hacker_update.py — Terminal-Only Matrix / Cyberpunk Auto-Update Script
========================================================================
Runs inside a terminal console with glowing green text and matrix hacking
visuals. Refreshes the GitHub contribution scoreboard and auto-closes.
"""

import datetime
import os
import random
import subprocess
import sys
import time

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")

# ANSI Color Codes for Glowing Terminal Green
G_BRIGHT = "\033[1;32m"
G_DIM    = "\033[2;32m"
G_ACCENT = "\033[1;96m"
RESET    = "\033[0m"


def enable_windows_ansi():
    """Enables ANSI color processing on Windows terminal console."""
    if sys.platform == "win32":
        os.system("color 0A")
        os.system("title SYSTEM OVERRIDE // BLAZE GITHUB PROFILE SYNC")


def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def matrix_stream_effect(lines=6, delay=0.03):
    """Simulates a fast hacking matrix code stream in green text."""
    chars = "0101010101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+=-_<>/"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(70))
        print(f"{G_DIM}{line}{RESET}")
        time.sleep(delay)


def print_banner():
    banner = f"""
{G_BRIGHT}
  ██████╗ ██╗      █████╗ ███████╗███████╗
  ██╔══██╗██║     ██╔══██╗╚══███╔╝██╔════╝
  ██████╔╝██║     ███████║  ███╔╝ █████╗  
  ██╔══██╗██║     ██╔══██║ ███╔╝  ██╔══╝  
  ██████╔╝███████╗██║  ██║███████╗███████╗
  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
  [ SYSTEM OVERRIDE // BLAZE GITHUB READ-ME SCOREBOARD SYNC ]
{RESET}
"""
    print(banner)


def log_step(text, symbol="[▶]"):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{G_BRIGHT}{symbol} [{ts}] {text}{RESET}")


def main():
    enable_windows_ansi()
    clear_screen()
    print_banner()
    time.sleep(0.3)

    print(f"{G_BRIGHT}======================================================================{RESET}")
    log_step("SYSTEM OVERRIDE INITIATED // TARGET: blazecodeprakhar", "[⚡]")
    print(f"{G_BRIGHT}======================================================================{RESET}")
    print()

    try:
        # Step 1
        matrix_stream_effect(4)
        log_step("BYPASSING GITHUB RATE-LIMIT FIREWALL...")
        log_step("Fetching contribution metrics from GitHub API...", "[+]")
        fetch_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "fetch_contributions.py")]
        res1 = subprocess.run(fetch_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if res1.returncode != 0:
            print(f"{G_DIM}[!] Warning fetching contributions: {res1.stderr.strip()}{RESET}")
        else:
            log_step("GitHub contribution metrics sync complete.", "[✔]")
        print()

        # Step 2
        matrix_stream_effect(4)
        log_step("RE-RENDERING HEATMAP SVG MATRIX...")
        log_step("Compiling animated contribution heatmap SVG artwork...", "[+]")
        render_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "render_heatmap_svg.py")]
        res2 = subprocess.run(render_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if res2.returncode != 0:
            print(f"{G_DIM}[!] Warning rendering heatmap: {res2.stderr.strip()}{RESET}")
        else:
            log_step("Animated contribution heatmap SVG compiled.", "[✔]")
        print()

        # Step 3
        matrix_stream_effect(4)
        log_step("GENERATING STREAK VISUAL MATRIX...")
        log_step("Generating streak SVG metrics...", "[+]")
        streak_out = os.path.join(REPO_ROOT, "streak.svg")
        streak_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "generate_streak_svg.py"), "blazecodeprakhar", streak_out]
        res3 = subprocess.run(streak_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if res3.returncode != 0:
            print(f"{G_DIM}[!] Warning generating streak: {res3.stderr.strip()}{RESET}")
        else:
            log_step("Contribution streak SVG generated.", "[✔]")
        print()

        # Git operations
        matrix_stream_effect(4)
        log_step("STAGING PAYLOAD & COMMITTING TO MAIN BRANCH...")
        subprocess.run(["git", "add", "-A"], cwd=REPO_ROOT, capture_output=True)

        status = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True)
        if not status.stdout.strip():
            log_step("Scoreboard is already up to date on origin/main.", "[i]")
        else:
            log_step("Committing payload: 'chore: refresh contribution graph [skip ci]'...", "[+]")
            subprocess.run(["git", "commit", "-m", "chore: refresh contribution graph [skip ci]"], cwd=REPO_ROOT, capture_output=True)

            log_step("Transmitting graphics payload to origin/main...", "[+]")
            push_res = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_ROOT, capture_output=True, text=True)
            if push_res.returncode != 0:
                log_step("Main push attempt deferred, trying master branch...", "[!]")
                push_res = subprocess.run(["git", "push", "origin", "master"], cwd=REPO_ROOT, capture_output=True, text=True)
            
            if push_res.returncode == 0:
                log_step("PAYLOAD SUCCESSFULLY DELIVERED TO GITHUB ORIGIN!", "[✔]")
            else:
                print(f"{G_DIM}[!] Push completed with message: {push_res.stderr.strip()}{RESET}")

        print()
        matrix_stream_effect(6)
        print()
        victory_box = f"""
{G_BRIGHT}
  ┌──────────────────────────────────────────────────────────────────┐
  │  [✔] ACCESS GRANTED // READ-ME SCOREBOARD UPDATED ON GITHUB      │
  │      TERMINAL AUTO-DISAPPEARING IN 3 SECONDS...                  │
  └──────────────────────────────────────────────────────────────────┘
{RESET}
"""
        print(victory_box)
        time.sleep(3.0)

    except Exception as e:
        print(f"\n{G_BRIGHT}[❌] CRITICAL OVERRIDE ERROR: {str(e)}{RESET}")
        time.sleep(5.0)


if __name__ == "__main__":
    main()
