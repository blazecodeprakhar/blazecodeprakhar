#!/usr/bin/env python3
"""
setup_schedule.py — Windows Task Scheduler Installer for 11:11 PM Daily Update
==============================================================================
Registers a Windows Scheduled Task named 'BlazeCodePrakharReadmeAutoUpdate' that
triggers 'hacker_update.py' every day at 11:11 PM (23:11).
"""

import argparse
import os
import subprocess
import sys

TASK_NAME = "BlazeCodePrakharReadmeAutoUpdate"
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
HACKER_SCRIPT = os.path.join(REPO_ROOT, "hacker_update.py")


def get_python_exe():
    """Returns path to pythonw.exe if available, else python.exe."""
    python_dir = os.path.dirname(sys.executable)
    pythonw = os.path.join(python_dir, "pythonw.exe")
    if os.path.exists(pythonw):
        return f'"{pythonw}"'
    return f'"{sys.executable}"'


def install_task(time_str="23:11"):
    py_exe = get_python_exe()
    cmd = (
        f'schtasks /create /tn "{TASK_NAME}" '
        f'/tr \'{py_exe} "{HACKER_SCRIPT}"\' '
        f'/sc daily /st {time_str} /f'
    )
    print(f"[*] Registering Windows Scheduled Task '{TASK_NAME}' for daily execution at {time_str}...")
    
    # Run schtasks
    result = subprocess.run(
        [
            "schtasks", "/create",
            "/tn", TASK_NAME,
            "/tr", f'{py_exe} "{HACKER_SCRIPT}"',
            "/sc", "daily",
            "/st", time_str,
            "/f"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"[OK] SUCCESS: Scheduled task '{TASK_NAME}' registered successfully!")
        print(f"     - Schedule: Daily @ {time_str} (11:11 PM)")
        print(f"     - Target Script: {HACKER_SCRIPT}")
    else:
        print(f"[ERROR] Error registering task: {result.stderr.strip()}")
        sys.exit(result.returncode)


def uninstall_task():
    print(f"[*] Removing Scheduled Task '{TASK_NAME}'...")
    result = subprocess.run(
        ["schtasks", "/delete", "/tn", TASK_NAME, "/f"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"[OK] Task '{TASK_NAME}' removed successfully.")
    else:
        print(f"[!] Warning/Error removing task: {result.stderr.strip()}")


def status_task():
    print(f"[*] Checking status for Scheduled Task '{TASK_NAME}'...")
    result = subprocess.run(
        ["schtasks", "/query", "/tn", TASK_NAME, "/v", "/fo", "LIST"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"[!] Task '{TASK_NAME}' is not registered or error querying: {result.stderr.strip()}")


def main():
    parser = argparse.ArgumentParser(description="Windows Task Scheduler Installer for Blaze Profile Readme Auto-Update")
    parser.add_argument("--uninstall", action="store_true", help="Remove the scheduled task")
    parser.add_argument("--status", action="store_true", help="Query status of the scheduled task")
    parser.add_argument("--time", default="23:11", help="Daily trigger time (HH:MM in 24h format, default 23:11)")
    args = parser.parse_args()

    if args.uninstall:
        uninstall_task()
    elif args.status:
        status_task()
    else:
        install_task(args.time)


if __name__ == "__main__":
    main()
