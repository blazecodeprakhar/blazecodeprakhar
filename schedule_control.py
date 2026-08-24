#!/usr/bin/env python3
"""
schedule_control.py — Interactive Scheduler Control Panel for Blaze Profile Readme Auto-Update
============================================================================================
Open this file to Turn ON, Turn OFF, Customize Schedule Timing, or Test Run the Matrix Hacker Update.
"""

import os
import re
import subprocess
import sys
import time

TASK_NAME = "BlazeCodePrakharReadmeAutoUpdate"
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
HACKER_SCRIPT = os.path.join(REPO_ROOT, "hacker_update.py")

# ANSI Colors
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"


def enable_ansi():
    if sys.platform == "win32":
        os.system("color 0A")
        os.system("title BLAZE AUTO-UPDATE // SCHEDULE CONTROL PANEL")


def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def get_task_info():
    """Queries Windows Task Scheduler and returns (is_registered, is_enabled, next_run, start_time)."""
    if sys.platform != "win32":
        return False, False, "N/A", "N/A"

    result = subprocess.run(
        ["schtasks", "/query", "/tn", TASK_NAME, "/v", "/fo", "LIST"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        return False, False, "Not Scheduled", "N/A"

    stdout = result.stdout
    is_registered = True
    is_enabled = "Scheduled Task State:                 Enabled" in stdout or "State:                                Enabled" in stdout or "Ready" in stdout
    
    # Extract Start Time
    match_time = re.search(r"Start Time:\s+([0-9:]+)", stdout)
    start_time = match_time.group(1) if match_time else "23:11:00"

    # Extract Next Run Time
    match_next = re.search(r"Next Run Time:\s+([0-9\/\:\-\s\w]+)", stdout)
    next_run = match_next.group(1).strip() if match_next else "N/A"

    return is_registered, is_enabled, next_run, start_time


def turn_on_schedule(time_str="23:11"):
    """Registers and enables the scheduled task for 11:11 PM (or custom time)."""
    tr_command = f'cmd.exe /c start "SYSTEM OVERRIDE" "{sys.executable}" "{HACKER_SCRIPT}"'
    
    print(f"\n[*] Registering Windows Scheduled Task '{TASK_NAME}' at {time_str}...")
    
    result = subprocess.run(
        [
            "schtasks", "/create",
            "/tn", TASK_NAME,
            "/tr", tr_command,
            "/sc", "daily",
            "/st", time_str,
            "/f"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{GREEN}[OK] SUCCESS: Auto-Update is now TURNED ON!{RESET}")
        print(f"{GREEN}     - Daily Schedule Time: {time_str} (11:11 PM){RESET}")
        print(f"{GREEN}     - Target Script: {HACKER_SCRIPT}{RESET}")
    else:
        print(f"{RED}[ERROR] Failed to turn on task: {result.stderr.strip()}{RESET}")


def turn_off_schedule():
    """Unregisters/disables the scheduled task."""
    print(f"\n[*] Turning OFF Auto-Update Scheduled Task '{TASK_NAME}'...")
    result = subprocess.run(
        ["schtasks", "/delete", "/tn", TASK_NAME, "/f"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"{GREEN}[OK] SUCCESS: Auto-Update feature is now TURNED OFF.{RESET}")
    else:
        print(f"{YELLOW}[!] Task is not currently active or already removed: {result.stderr.strip()}{RESET}")


def customize_time():
    """Prompts user for custom HH:MM execution time."""
    print("\n------------------------------------------------------------")
    print(" CUSTOMIZE DAILY EXECUTION TIME")
    print(" Enter time in 24-hour HH:MM format.")
    print(" Examples: 23:11 (11:11 PM), 22:00 (10:00 PM), 09:30 (9:30 AM)")
    print("------------------------------------------------------------")
    user_input = input(" Enter New Time [HH:MM] (Press Enter for default 23:11): ").strip()
    
    if not user_input:
        user_input = "23:11"
    
    # Validate HH:MM format
    if not re.match(r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$", user_input):
        print(f"{RED}[!] Invalid time format. Please use HH:MM format (e.g., 23:11).{RESET}")
        return

    # Add leading zero if needed (e.g. 9:30 -> 09:30)
    parts = user_input.split(":")
    formatted_time = f"{int(parts[0]):02d}:{int(parts[1]):02d}"

    turn_on_schedule(formatted_time)


def run_test_now():
    """Runs hacker_update.py immediately in a green matrix terminal window for testing."""
    print(f"\n{CYAN}[*] Triggering Matrix Hacker Update now...{RESET}")
    cmd = f'cmd.exe /c start "SYSTEM OVERRIDE" "{sys.executable}" "{HACKER_SCRIPT}"'
    subprocess.run(cmd, shell=True)
    print(f"{GREEN}[OK] Hacker terminal window launched!{RESET}")


def main_menu():
    enable_ansi()
    
    while True:
        clear_screen()
        is_registered, is_enabled, next_run, start_time = get_task_info()

        print(f"{GREEN}======================================================================")
        print(f" [⚡] BLAZE PROFILE READ-ME AUTO-UPDATE // CONTROL PANEL")
        print(f"======================================================================{RESET}")
        
        if is_registered and is_enabled:
            status_str = f"{GREEN}● ON / ENABLED{RESET} (Daily @ {start_time})"
        else:
            status_str = f"{RED}○ OFF / DISABLED{RESET}"

        print(f" Automatic Feature Status: {status_str}")
        print(f" Next Scheduled Execution: {CYAN}{next_run}{RESET}")
        print(f" Target Hacker Script   : {HACKER_SCRIPT}")
        print("----------------------------------------------------------------------")
        print(" SELECT AN OPTION:")
        print(f"  {GREEN}[1]{RESET} Turn ON Auto-Update (Set to 11:11 PM Daily)")
        print(f"  {RED}[2]{RESET} Turn OFF Auto-Update (Disable Automatic Feature)")
        print(f"  {YELLOW}[3]{RESET} Customize Execution Time (Set custom HH:MM time)")
        print(f"  {CYAN}[4]{RESET} Run Matrix Hacker Update Now (Manual Test Run)")
        print(f"  [5] Exit Control Panel")
        print("----------------------------------------------------------------------")
        
        choice = input(" Enter Option (1-5): ").strip()

        if choice == "1":
            turn_on_schedule("23:11")
            input("\n Press Enter to return to main menu...")
        elif choice == "2":
            turn_off_schedule()
            input("\n Press Enter to return to main menu...")
        elif choice == "3":
            customize_time()
            input("\n Press Enter to return to main menu...")
        elif choice == "4":
            run_test_now()
            input("\n Press Enter to return to main menu...")
        elif choice == "5":
            print(f"\n{GREEN}[*] Exiting Control Panel. Goodbye, Blaze!{RESET}")
            time.sleep(0.5)
            break
        else:
            print(f"{RED}[!] Invalid choice. Please enter a number between 1 and 5.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()
