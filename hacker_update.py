#!/usr/bin/env python3
"""
hacker_update.py — Terminal-Only Green Matrix Hacker Auto-Update Script
========================================================================
Runs inside a terminal console with 100% glowing green text, loud crisp in-memory
WAV sci-fi digital electric typing sound effects, crisp alignment, and auto-close.
"""

import datetime
import io
import math
import os
import random
import struct
import subprocess
import sys
import time

try:
    import winsound
    import wave
    HAS_SOUND = True
except ImportError:
    HAS_SOUND = False

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")

# ANSI Color Codes for 100% Glowing Terminal Green
G_BRIGHT = "\033[1;32m"
G_DIM    = "\033[2;32m"
RESET    = "\033[0m"


def generate_wav_bytes(frequencies, total_samples=600, decay_rate=150, volume=22000):
    """Generates a crisp in-memory WAV byte stream for loud sci-fi digital sound effects."""
    buf = io.BytesIO()
    w = wave.open(buf, 'wb')
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    
    samples = []
    num_freqs = len(frequencies)
    samples_per_freq = total_samples // num_freqs
    
    for idx, freq in enumerate(frequencies):
        for i in range(samples_per_freq):
            t = i / 44100.0
            # Sine wave with exponential decay envelope for ultra-crisp digital click
            env = math.exp(-i / decay_rate)
            val = int(volume * env * math.sin(2 * math.pi * freq * t))
            samples.append(val)
            
    w.writeframes(struct.pack('<' + 'h' * len(samples), *samples))
    w.close()
    return buf.getvalue()


# Pre-generate high-definition sci-fi digital sound samples
if HAS_SOUND:
    try:
        # Sharp high-frequency electric typing clicks
        CLICK_WAV_1 = generate_wav_bytes([2600], total_samples=550, decay_rate=100)
        CLICK_WAV_2 = generate_wav_bytes([3200], total_samples=550, decay_rate=100)
        CLICK_WAV_3 = generate_wav_bytes([3800], total_samples=550, decay_rate=100)
        CLICK_VARIANTS = [CLICK_WAV_1, CLICK_WAV_2, CLICK_WAV_3]

        # Sci-Fi step telemetry chirp
        CHIRP_WAV = generate_wav_bytes([1800, 3200], total_samples=1200, decay_rate=250)

        # Sci-Fi access granted victory chime
        SUCCESS_WAV = generate_wav_bytes([1600, 2400, 3200, 4200], total_samples=3000, decay_rate=400)
    except Exception:
        HAS_SOUND = False


def play_click():
    """Plays sharp digital electric typing click sound."""
    if HAS_SOUND:
        try:
            wav_data = random.choice(CLICK_VARIANTS)
            winsound.PlaySound(wav_data, winsound.SND_MEMORY | winsound.SND_ASYNC)
        except Exception:
            pass


def play_chirp():
    """Plays sci-fi step activation telemetry chirp."""
    if HAS_SOUND:
        try:
            winsound.PlaySound(CHIRP_WAV, winsound.SND_MEMORY | winsound.SND_ASYNC)
        except Exception:
            pass


def play_success_chime():
    """Plays sci-fi victory completion chime."""
    if HAS_SOUND:
        try:
            winsound.PlaySound(SUCCESS_WAV, winsound.SND_MEMORY | winsound.SND_ASYNC)
        except Exception:
            pass


def enable_windows_ansi():
    """Enables ANSI color processing and green console palette on Windows."""
    if sys.platform == "win32":
        os.system("color 0A")
        os.system("title SYSTEM OVERRIDE // BLAZE GITHUB PROFILE SYNC")


def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def hacker_typing_print(text, color=G_BRIGHT, char_delay=0.003, sound_freq=1):
    """Prints character-by-character with loud, crisp digital electric typing sound effects."""
    sys.stdout.write(color)
    sys.stdout.flush()
    for idx, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        if idx % sound_freq == 0 and char not in " \n\r\t":
            play_click()
        time.sleep(char_delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


def matrix_stream_effect(lines=5, delay=0.015):
    """Fast hacking matrix code stream with crisp digital micro-zaps."""
    chars = "0101010101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+=-_<>/"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(70))
        sys.stdout.write(f"{G_DIM}{line}{RESET}\n")
        sys.stdout.flush()
        play_click()
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
        hacker_typing_print(line, color=G_BRIGHT, char_delay=0.001, sound_freq=2)


def log_step(text, symbol="[+]"):
    """Prints perfectly aligned log step with loud digital telemetry audio."""
    play_chirp()
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    tag = f"{symbol:<4}"
    full_str = f"{tag} [{ts}] {text}"
    hacker_typing_print(full_str, color=G_BRIGHT, char_delay=0.003, sound_freq=1)


def main():
    enable_windows_ansi()
    clear_screen()
    print_banner()
    time.sleep(0.15)

    hacker_typing_print("======================================================================", G_BRIGHT, 0.001, 4)
    log_step("SYSTEM OVERRIDE INITIATED // TARGET: blazecodeprakhar", "[*]")
    hacker_typing_print("======================================================================", G_BRIGHT, 0.001, 4)
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

        play_success_chime()
        victory_box = [
            "  ┌──────────────────────────────────────────────────────────────────┐",
            "  │  [OK] ACCESS GRANTED // READ-ME SCOREBOARD UPDATED ON GITHUB     │",
            "  │       TERMINAL AUTO-DISAPPEARING IN 3 SECONDS...                 │",
            "  └──────────────────────────────────────────────────────────────────┘"
        ]
        for line in victory_box:
            hacker_typing_print(line, color=G_BRIGHT, char_delay=0.001, sound_freq=2)

        time.sleep(3.0)

    except Exception as e:
        print(f"\n{G_BRIGHT}[!] CRITICAL OVERRIDE ERROR: {str(e)}{RESET}")
        time.sleep(5.0)


if __name__ == "__main__":
    main()
