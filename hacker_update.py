#!/usr/bin/env python3
"""
hacker_update.py — Matrix / Cyberpunk Auto-Update GUI Interface
=================================================================
Runs the GitHub contribution scoreboard refresh pipeline inside a high-tech
hacker terminal GUI. Automatically closes upon successful execution.
"""

import datetime
import os
import random
import subprocess
import sys
import threading
import time
import tkinter as tk
from tkinter import font

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")

class MatrixHackerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTEM OVERRIDE // BLAZE PROFILE SYNC")
        
        # Dimensions & Centering
        self.width = 760
        self.height = 540
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws // 2) - (self.width // 2)
        y = (hs // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.resizable(False, False)
        self.root.configure(bg="#050a0e")
        self.root.attributes("-topmost", True)

        # Fonts
        self.term_font = ("Consolas", 11, "bold")
        self.title_font = ("Consolas", 14, "bold")

        # Canvas for Matrix Rain Background
        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg="#050a0e",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        # Matrix Rain Drops
        self.cols = 40
        self.drops = [random.randint(-20, 0) for _ in range(self.cols)]
        self.matrix_chars = "0101010101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+=-_<>/"

        # Foreground Terminal Frame
        self.term_frame = tk.Frame(
            self.canvas,
            bg="#0b131b",
            bd=2,
            relief="solid",
            highlightbackground="#00ff66",
            highlightthickness=1
        )
        self.canvas.create_window(
            self.width // 2,
            self.height // 2,
            window=self.term_frame,
            width=700,
            height=460
        )

        # Header Bar
        self.header_label = tk.Label(
            self.term_frame,
            text="[⚡ BLAZE CYBERNETIC MATRIX // AUTOMATED README OVERRIDE ⚡]",
            fg="#00e5ff",
            bg="#0b131b",
            font=self.title_font,
            anchor="w",
            padx=15,
            pady=10
        )
        self.header_label.pack(fill="x")

        # Status Bar
        self.status_bar = tk.Label(
            self.term_frame,
            text="STATUS: INITIALIZING SYSTEM INTERFACE...",
            fg="#00ff66",
            bg="#111d28",
            font=("Consolas", 10, "bold"),
            anchor="w",
            padx=15,
            pady=4
        )
        self.status_bar.pack(fill="x")

        # Terminal Text View
        self.text_box = tk.Text(
            self.term_frame,
            bg="#060c12",
            fg="#00ff66",
            insertbackground="#00ff66",
            font=self.term_font,
            bd=0,
            padx=15,
            pady=15,
            highlightthickness=0
        )
        self.text_box.pack(fill="both", expand=True)
        self.text_box.config(state="disabled")

        # Start animations and pipeline thread
        self.running = True
        self.animate_matrix()
        
        # Start pipeline after 500ms
        self.root.after(500, self.start_pipeline)

    def animate_matrix(self):
        if not self.running:
            return
        self.canvas.delete("matrix")
        for i in range(len(self.drops)):
            char = random.choice(self.matrix_chars)
            x = i * 19 + 8
            y = self.drops[i] * 18
            
            # Draw green matrix char on canvas background
            if 0 <= y <= self.height:
                color = "#00ff66" if random.random() > 0.15 else "#ffffff"
                self.canvas.create_text(
                    x, y, text=char, fill=color, font=("Consolas", 10), tags="matrix"
                )
            
            self.drops[i] += 1
            if self.drops[i] * 18 > self.height and random.random() > 0.95:
                self.drops[i] = 0

        self.root.after(60, self.animate_matrix)

    def log(self, text, tag=None):
        def _log():
            self.text_box.config(state="normal")
            ts = datetime.datetime.now().strftime("%H:%M:%S")
            self.text_box.insert("end", f"[{ts}] {text}\n", tag)
            self.text_box.see("end")
            self.text_box.config(state="disabled")

        self.root.after(0, _log)

    def set_status(self, text, color="#00ff66"):
        def _set():
            self.status_bar.config(text=f"STATUS: {text}", fg=color)
        self.root.after(0, _set)

    def start_pipeline(self):
        threading.Thread(target=self.run_execution_steps, daemon=True).start()

    def run_execution_steps(self):
        try:
            self.log("==================================================")
            self.log(" SYSTEM OVERRIDE INITIATED // USER: blazecodeprakhar")
            self.log("==================================================")
            time.sleep(0.4)

            # Step 1
            self.set_status("BYPASSING GITHUB RATE-LIMIT FIREWALL...")
            self.log("[+] Step 1/3: Fetching contribution metrics from GitHub API...")
            fetch_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "fetch_contributions.py")]
            res1 = subprocess.run(fetch_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
            if res1.returncode != 0:
                self.log(f"[!] Warning fetching contributions: {res1.stderr.strip()}")
            else:
                self.log("[✔] GitHub contribution metrics sync complete.")
            time.sleep(0.4)

            # Step 2
            self.set_status("RE-RENDERING HEATMAP SVG MATRIX...")
            self.log("[+] Step 2/3: Rendering animated heatmap SVG artwork...")
            render_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "render_heatmap_svg.py")]
            res2 = subprocess.run(render_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
            if res2.returncode != 0:
                self.log(f"[!] Warning rendering heatmap: {res2.stderr.strip()}")
            else:
                self.log("[✔] Animated contribution heatmap SVG compiled.")
            time.sleep(0.4)

            # Step 3
            self.set_status("GENERATING STREAK VISUAL MATRIX...")
            self.log("[+] Step 3/3: Generating streak SVG stats...")
            streak_out = os.path.join(REPO_ROOT, "streak.svg")
            streak_cmd = [sys.executable, os.path.join(SCRIPTS_DIR, "generate_streak_svg.py"), "blazecodeprakhar", streak_out]
            res3 = subprocess.run(streak_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
            if res3.returncode != 0:
                self.log(f"[!] Warning generating streak: {res3.stderr.strip()}")
            else:
                self.log("[✔] Contribution streak SVG generated.")
            time.sleep(0.4)

            # Git operations
            self.set_status("STAGING PAYLOAD & COMMITTING TO MAIN...")
            self.log("[+] Staging changed SVG vector assets (git add -A)...")
            subprocess.run(["git", "add", "-A"], cwd=REPO_ROOT, capture_output=True)

            status = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True)
            if not status.stdout.strip():
                self.log("[i] Scoreboard is already fully up to date on origin/main.")
            else:
                self.log("[+] Committing payload: 'chore: refresh contribution graph [skip ci]'...")
                subprocess.run(["git", "commit", "-m", "chore: refresh contribution graph [skip ci]"], cwd=REPO_ROOT, capture_output=True)

                self.set_status("TRANSMITTING TO GITHUB ORIGIN/MAIN...", "#00e5ff")
                self.log("[+] Pushing updated graphics payload to origin/main...")
                push_res = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_ROOT, capture_output=True, text=True)
                if push_res.returncode != 0:
                    self.log("[!] Main push attempt deferred, trying master branch...")
                    push_res = subprocess.run(["git", "push", "origin", "master"], cwd=REPO_ROOT, capture_output=True, text=True)
                
                if push_res.returncode == 0:
                    self.log("[✔] PAYLOAD SUCCESSFULLY DELIVERED TO GITHUB ORIGIN!")
                else:
                    self.log(f"[!] Push completed with message: {push_res.stderr.strip()}")

            time.sleep(0.5)
            self.set_status("ACCESS GRANTED // SCOREBOARD UPDATE COMPLETE", "#00ff66")
            self.log("==================================================")
            self.log(" [✔] OVERRIDE SUCCESSFUL — DISAPPEARING IN 3 SECONDS...")
            self.log("==================================================")

            # Auto close window after 3 seconds
            time.sleep(3.0)
            self.running = False
            self.root.after(0, self.root.destroy)

        except Exception as e:
            self.set_status("OVERRIDE ERROR ENCOUNTERED", "#ff3366")
            self.log(f"[❌] CRITICAL ERROR: {str(e)}")
            time.sleep(5.0)
            self.running = False
            self.root.after(0, self.root.destroy)


def main():
    root = tk.Tk()
    app = MatrixHackerUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
