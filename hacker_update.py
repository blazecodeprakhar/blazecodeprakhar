#!/usr/bin/env python3
"""
hacker_update.py — Terminal-Only Green Matrix Hacker Auto-Update Script
========================================================================
Runs inside a terminal console with 100% glowing green text, sci-fi binary code
interface sound effects (bi-tonal data processing beeps), crisp alignment, and auto-close.
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

# ANSI Color Codes for 100% Glowing Terminal Green
G_BRIGHT = "\033[1;32m"
G_DIM    = "\033[2;32m"
RESET    = "\033[0m"


def play_beep(freq, duration_ms):
    """Plays a micro frequency pulse asynchronously on Windows."""
    if HAS_SOUND:
        try:
            threading.Thread(
                target=winsound.Beep,
                args=(int(freq), int(duration_ms)),
                daemon=True
            ).start()
        except Exception:
            pass


def play_binary_data_sound():
    """
    Sci-Fi Binary Code & Data Processing Sound Effect:
    Alternates between high binary bit (3500Hz) and low binary bit (1750Hz)
    micro-beeps, simulating a sci-fi computer processing 0s and 1s.
    """
    bit_freq = random.choice([1750, 2200, 3100, 3800, 4400])
    play_beep(bit_freq, 5)


def play_scifi_step_chirp():
    """Sci-Fi computer telemetry dual-tone step sound."""
    if not HAS_SOUND:
        return
    def _chirp():
        for f in [2400, 3600]:
            try:
                winsound.Beep(f, 12)
            except Exception:
                pass
    threading.Thread(target=_chirp, daemon=True).start()


def play_scifi_access_granted():
    """Sci-Fi computer interface confirmation telemetry chime."""
    if not HAS_SOUND:
        return
    def _chime():
        for f in [1800, 2400, 3200, 4200]:
            try:
                winsound.Beep(f, 25)
            except Exception:
                pass
            time.sleep(0.01)
    threading.Thread(target=_chime, daemon=True).start()


def enable_windows_ansi():
    """Enables ANSI color processing and green console palette on Windows."""
    if sys.platform == "win32":
        os.system("color 0A")
        os.system("title SYSTEM OVERRIDE // BLAZE GITHUB PROFILE SYNC")


def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def hacker_typing_print(text, color=G_BRIGHT, char_delay=0.003, sound_freq=2):
    """Character-by-character printing with sci-fi binary data processing sounds."""
    sys.stdout.write(color)
    sys.stdout.flush()
    for idx, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        if idx % sound_freq == 0 and char not in " \n\r\t":
            play_binary_data_sound()
        time.sleep(char_delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


def matrix_stream_effect(lines=5, delay=0.015):
    """Fast hacking matrix code stream with sci-fi binary data processing beeps."""
    chars = "0101010101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+=-_<>/"
    for i in range(lines):
        line = "".join(random.choice(chars) for _ in range(70))
        sys.stdout.write(f"{G_DIM}{line}{RESET}\n")
        sys.stdout.flush()
        # Sci-Fi binary stream telemetry sound
        play_binary_data_sound()
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
        hacker_typing_print(line, color=G_BRIGHT, char_delay=0.001, sound_freq=3)


def log_step(text, symbol="[+]"):
    """Prints perfectly aligned log step in 100% bright green text with sci-fi chirp."""
    play_scifi_step_chirp()
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    tag = f"{symbol:<4}"
    full_str = f"{tag} [{ts}] {text}"
    hacker_typing_print(full_str, color=G_BRIGHT, char_delay=0.003, sound_freq=2)


def main():
    enable_windows_ansi()
    clear_screen()
    print_banner()
    time.sleep(0.15)

    hacker_typing_print("======================================================================", G_BRIGHT, 0.001, 8)
    log_step("SYSTEM OVERRIDE INITIATED // TARGET: blazecodeprakhar", "[*]")
    hacker_typing_print("======================================================================", G_BRIGHT, 0.001, 8)
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
            log_step("GitHub contribution metrics sync complete.", "[OK]")
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
            log_step("Animated contribution heatmap SVG compiled.", "[OK]")
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
            log_step("Contribution streak SVG generated.", "[OK]")
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
                log_step("PAYLOAD SUCCESSFULLY DELIVERED TO GITHUB ORIGIN!", "[OK]")
            else:
                print(f"{G_DIM}[!] Push completed with message: {push_res.stderr.strip()}{RESET}")

        print()
        matrix_stream_effect(6)
        print()

        play_scifi_access_granted()
        victory_box = [
            "  ┌──────────────────────────────────────────────────────────────────┐",
            "  │  [OK] ACCESS GRANTED // READ-ME SCOREBOARD UPDATED ON GITHUB     │",
            "  │       TERMINAL AUTO-DISAPPEARING IN 3 SECONDS...                 │",
            "  └──────────────────────────────────────────────────────────────────┘"
        ]
        for line in victory_box:
            hacker_typing_print(line, color=G_BRIGHT, char_delay=0.002, sound_freq=3)

        time.sleep(3.0)

    except Exception as e:
        print(f"\n{G_BRIGHT}[!] CRITICAL OVERRIDE ERROR: {str(e)}{RESET}")
        time.sleep(5.0)


if __name__ == "__main__":
    main()
