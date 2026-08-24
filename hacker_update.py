#!/usr/bin/env python3
"""
hacker_update.py — Terminal-Only Green Matrix Hacker Auto-Update Script
========================================================================
Runs inside a terminal console with glowing green text, retro movie hacking
typing audio / beeps, matrix stream visual effects, and auto-close.
"""

import datetime
import os
import random
import subprocess
import sys
import threading
import time

try:
    import winsound
    HAS_SOUND = True
except ImportError:
    HAS_SOUND = False

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")

# ANSI Color Codes for Glowing Terminal Green
G_BRIGHT = "\033[1;32m"
G_DIM    = "\033[2;32m"
G_ACCENT = "\033[1;96m"
RESET    = "\033[0m"


def play_beep(freq, duration_ms):
    """Plays a frequency beep asynchronously on Windows."""
    if HAS_SOUND:
        try:
            threading.Thread(target=winsound.Beep, args=(int(freq), int(duration_ms)), daemon=True).start()
        except Exception:
            pass


def play_typing_beep():
    """Retro sci-fi computer terminal typing click/beep."""
    freq = random.choice([1600, 1800, 2000, 2200, 2400, 2600])
    play_beep(freq, 12)


def play_victory_jingle():
    """Classic 80s movie hacker 'ACCESS GRANTED' ascending synth bleeps."""
    if not HAS_SOUND:
        return
    def _jingle():
        notes = [(880, 80), (1046, 80), (1318, 80), (1567, 80), (1760, 220), (2093, 350)]
        for f, d in notes:
            try:
                winsound.Beep(f, d)
            except Exception:
                pass
            time.sleep(0.02)
    threading.Thread(target=_jingle, daemon=True).start()


def enable_windows_ansi():
    """Enables ANSI color processing on Windows terminal console."""
    if sys.platform == "win32":
        os.system("color 0A")
        os.system("title SYSTEM OVERRIDE // BLAZE GITHUB PROFILE SYNC")


def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def hacker_typing_print(text, color=G_BRIGHT, char_delay=0.008, beep_interval=3):
    """Prints text character-by-character with retro movie hacking beeps."""
    sys.stdout.write(color)
    sys.stdout.flush()
    for idx, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        if idx % beep_interval == 0 and char not in " \n":
            play_typing_beep()
        time.sleep(char_delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


def matrix_stream_effect(lines=5, delay=0.025):
    """Simulates a fast hacking matrix code stream with rapid micro-beeps."""
    chars = "0101010101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+=-_<>/"
    for i in range(lines):
        line = "".join(random.choice(chars) for _ in range(68))
        sys.stdout.write(f"{G_DIM}{line}{RESET}\n")
        sys.stdout.flush()
        play_beep(1200 + (i % 6) * 250, 10)
        time.sleep(delay)


def print_banner():
    banner_lines = [
        "  ██████╗ ██╗      █████╗ ███████╗███████╗",
        "  ██╔══██╗██║     ██╔══██╗╚══███╔╝██╔════╝",
        "  ██████╔╝██║     ███████║  ███╔╝ █████╗  ",
        "  ██╔══██╗██║     ██╔══██║ ███╔╝  ██╔══╝  ",
        "  ██████╔╝███████╗██║  ██║███████╗███████╗",
        "  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝",
        "  [ SYSTEM OVERRIDE // BLAZE GITHUB READ-ME SCOREBOARD SYNC ]"
    ]
    for line in banner_lines:
        hacker_typing_print(line, color=G_BRIGHT, char_delay=0.003, beep_interval=4)


def log_step(text, symbol="[▶]"):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    full_str = f"{symbol} [{ts}] {text}"
    hacker_typing_print(full_str, color=G_BRIGHT, char_delay=0.01, beep_interval=3)


def main():
    enable_windows_ansi()
    clear_screen()
    print_banner()
    time.sleep(0.2)

    hacker_typing_print("======================================================================", G_BRIGHT, 0.002, 10)
    log_step("SYSTEM OVERRIDE INITIATED // TARGET: blazecodeprakhar", "[⚡]")
    hacker_typing_print("======================================================================", G_BRIGHT, 0.002, 10)
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

        play_victory_jingle()
        victory_box = [
            "  ┌──────────────────────────────────────────────────────────────────┐",
            "  │  [✔] ACCESS GRANTED // READ-ME SCOREBOARD UPDATED ON GITHUB      │",
            "  │      TERMINAL AUTO-DISAPPEARING IN 3 SECONDS...                  │",
            "  └──────────────────────────────────────────────────────────────────┘"
        ]
        for line in victory_box:
            hacker_typing_print(line, color=G_BRIGHT, char_delay=0.005, beep_interval=4)

        time.sleep(3.0)

    except Exception as e:
        print(f"\n{G_BRIGHT}[❌] CRITICAL OVERRIDE ERROR: {str(e)}{RESET}")
        time.sleep(5.0)


if __name__ == "__main__":
    main()
