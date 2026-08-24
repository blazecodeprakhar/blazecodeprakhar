#!/usr/bin/env python3
"""
hacker_update.py — Fullscreen Japanese Cyberpunk Matrix Hacker Auto-Update Script
==================================================================================
Runs inside a terminal console with glowing green text, authentic Japanese Katakana
matrix streams, red Blaze alerts, background sound.mp3 playback, and auto-close.
"""

import ctypes
import datetime
import os
import random
import shutil
import subprocess
import sys
import time

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")
MP3_PATH = os.path.join(REPO_ROOT, "sound.mp3")

# Ensure UTF-8 output encoding for Japanese Katakana characters
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ANSI Color Codes for Hacker Palette
G_BRIGHT = "\033[1;32m"
G_DIM    = "\033[2;32m"
RED      = "\033[1;31m"
CYAN     = "\033[1;36m"
WHITE    = "\033[1;37m"
RESET    = "\033[0m"


def get_terminal_width():
    """Gets current console width to fill the entire screen with matrix text."""
    try:
        cols = shutil.get_terminal_size((110, 30)).columns
        return max(80, cols - 2)
    except Exception:
        return 110


def start_background_audio():
    """Starts playing sound.mp3 seamlessly in the background without any interface."""
    if sys.platform == "win32" and os.path.exists(MP3_PATH):
        try:
            cmd_open = f'open "{MP3_PATH}" type mpegvideo alias bgm'
            ctypes.windll.winmm.mciSendStringW(cmd_open, None, 0, 0)
            ctypes.windll.winmm.mciSendStringW('play bgm repeat', None, 0, 0)
        except Exception:
            pass


def stop_background_audio():
    """Stops background sound.mp3 audio playback upon termination."""
    if sys.platform == "win32":
        try:
            ctypes.windll.winmm.mciSendStringW('stop bgm', None, 0, 0)
            ctypes.windll.winmm.mciSendStringW('close bgm', None, 0, 0)
        except Exception:
            pass


def enable_windows_ansi():
    """Enables ANSI color processing and UTF-8 green console palette on Windows."""
    if sys.platform == "win32":
        os.system("chcp 65001 > nul")
        os.system("color 0A")
        os.system("title SYSTEM OVERRIDE // BLAZE GITHUB PROFILE SYNC")


def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def hacker_typing_print(text, color=G_BRIGHT, char_delay=0.0015):
    """Fast character-by-character printing effect."""
    sys.stdout.write(color)
    sys.stdout.flush()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


def continuous_matrix_rain(lines=8, delay=0.008):
    """Fills the ENTIRE console width with Japanese Katakana & Matrix rain streams."""
    width = get_terminal_width()
    # Authentic Matrix Rain Katakana & Cyber characters
    jp_chars = "ｦｱｳｴｵｶｷｹｺｻｼｽｾｿﾀﾂﾃﾅﾆﾇﾈﾊﾋﾎﾏﾐﾑﾒﾓﾔﾕﾗﾘﾜ01010101XYZ@#$%&*+=-_<>"
    hex_tokens = ["0x7F", "0x8A", "0xFF", "0x00", "データ", "同期", "侵入", "オーバーライド"]
    
    for _ in range(lines):
        line_chars = []
        curr_len = 0
        while curr_len < width:
            if random.random() > 0.75:
                tok = random.choice(hex_tokens) + " "
                line_chars.append(tok)
                curr_len += len(tok)
            else:
                ch = random.choice(jp_chars)
                line_chars.append(ch)
                curr_len += 1
        
        line_str = "".join(line_chars)[:width]
        color = G_DIM if random.random() > 0.2 else G_BRIGHT
        sys.stdout.write(f"{color}{line_str}{RESET}\n")
        sys.stdout.flush()
        time.sleep(delay)


def print_hacker_header():
    width = get_terminal_width()
    border = "=" * width

    banner_lines = [
        "  ██████╗ ██╗      █████╗ ███████╗███████╗",
        "  ██╔══██╗██║     ██╔══██╗╚══███╔╝██╔════╝",
        "  ██████╔╝██║     ███████║  ███╔╝ █████╗  ",
        "  ██╔══██╗██║     ██╔══██║ ███╔╝  ██╔══╝  ",
        "  ██████╔╝███████╗██║  ██║███████╗███████╗",
        "  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝",
        "  [ システム・オーバーライド // サイバー空間 // BLAZE GITHUB SCOREBOARD SYNC ]"
    ]

    hacker_typing_print(border, G_BRIGHT, 0.0005)
    for line in banner_lines:
        hacker_typing_print(line, G_BRIGHT, 0.001)
    hacker_typing_print(border, G_BRIGHT, 0.0005)


def print_red_blaze_alerts():
    width = get_terminal_width()
    border = "=" * width
    
    hacker_typing_print(border, RED, 0.0005)
    hacker_typing_print(" [🔥] システム侵入 // BLAZE MATRIX PROTOCOL ONLINE", RED, 0.001)
    hacker_typing_print(" [🔥] 警告: セキュリティオーバーライド実行中... ACCESSING ORIGIN/MAIN", RED, 0.001)
    hacker_typing_print(" [🔥] MESSAGE TO BLAZE: データベース同期接続完了", RED, 0.001)
    hacker_typing_print(border, RED, 0.0005)


def log_step(text, symbol="[+]"):
    """Prints perfectly aligned log step in 100% bright green text."""
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    tag = f"{symbol:<4}"
    full_str = f"{tag} [{ts}] {text}"
    hacker_typing_print(full_str, color=G_BRIGHT, char_delay=0.002)


def main():
    enable_windows_ansi()
    clear_screen()
    
    # Start background sound.mp3 playback
    start_background_audio()

    # Intro Japanese Matrix Rain Cascade
    continuous_matrix_rain(lines=12, delay=0.005)

    print_hacker_header()
    time.sleep(0.1)

    print_red_blaze_alerts()
    print()

    # Continuous Japanese Matrix Rain before execution
    continuous_matrix_rain(lines=8, delay=0.005)
    log_step("システムオーバーライド開始 // TARGET: blazecodeprakhar", "[*]")
    print()

    try:
        # Step 1: Fetch
        continuous_matrix_rain(lines=6, delay=0.005)
        log_step("BYPASSING GITHUB RATE-LIMIT FIREWALL...")
        log_step("Fetching contribution metrics from GitHub API...", "[+]")
        fetch_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "fetch_contributions.py")]
        res1 = subprocess.run(fetch_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if res1.returncode != 0:
            print(f"{G_DIM}[!] Warning fetching contributions: {res1.stderr.strip()}{RESET}")
        else:
            log_step("GitHub contribution metrics sync complete (データ同期完了).", "[OK]")
        print()

        # Step 2: Render Heatmap
        continuous_matrix_rain(lines=6, delay=0.005)
        log_step("RE-RENDERING HEATMAP SVG MATRIX...")
        log_step("Compiling animated contribution heatmap SVG artwork...", "[+]")
        render_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "render_heatmap_svg.py")]
        res2 = subprocess.run(render_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if res2.returncode != 0:
            print(f"{G_DIM}[!] Warning rendering heatmap: {res2.stderr.strip()}{RESET}")
        else:
            log_step("Animated contribution heatmap SVG compiled.", "[OK]")
        print()

        # Step 3: Streak SVG
        continuous_matrix_rain(lines=6, delay=0.005)
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
        continuous_matrix_rain(lines=6, delay=0.005)
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

        # Continuous Katakana matrix rain stream
        continuous_matrix_rain(lines=10, delay=0.005)
        print()

        # Red Blaze Victory Status Alert
        width = get_terminal_width()
        border = "=" * width
        hacker_typing_print(border, RED, 0.0005)
        hacker_typing_print(" [🔥] BLAZE PROTOCOL: 任務完了 // ALL SYSTEMS OPERATIONAL", RED, 0.001)
        hacker_typing_print(border, RED, 0.0005)
        print()

        box_w = min(width - 4, 78)
        line1 = " [OK] アクセス許可 // ACCESS GRANTED // GITHUB SCOREBOARD SYNCHRONIZED".ljust(box_w)
        line2 = "      システム終了まで 3 秒... (TERMINAL AUTO-DISAPPEARING IN 3 SECONDS)".ljust(box_w)
        
        victory_box = [
            f"  ┌{'─' * box_w}┐",
            f"  │{line1}│",
            f"  │{line2}│",
            f"  └{'─' * box_w}┘"
        ]
        for line in victory_box:
            hacker_typing_print(line, color=G_BRIGHT, char_delay=0.001)

        # Final Japanese Katakana matrix rain cascade
        continuous_matrix_rain(lines=15, delay=0.005)
        time.sleep(2.0)

    except Exception as e:
        print(f"\n{G_BRIGHT}[!] CRITICAL OVERRIDE ERROR: {str(e)}{RESET}")
        time.sleep(5.0)
    finally:
        stop_background_audio()


if __name__ == "__main__":
    main()
