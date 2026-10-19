"""Launcher for the multi-function calculator and puzzle games.

Run from any directory:
    python FirstPage.py

Each menu item starts a small desktop program in a child process using the
current Python interpreter, so the app also works when it is launched from a
virtual environment and ``python`` is not on PATH.
"""
from __future__ import annotations

import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

BASE = Path(__file__).resolve().parent

MENU = [
    ("华容道游戏", "game_huarongdao.py"),
    ("数独游戏（Pygame）", "main.py"),
    ("科学计算器", "cal.py"),
    ("进制转换 / 斐波那契", "jinzhi.py"),
    ("猜数字 / 反应测试", "game_guess.py"),
    ("求解华容道（搜索）", "hr.py"),
    ("求解数独（回溯）", "soduku.py"),
    ("2048", "game_2048.py"),
]


def launch(filename: str) -> None:
    script = BASE / filename
    if not script.exists():
        messagebox.showerror("启动失败", f"找不到 {script.name}")
        return
    try:
        subprocess.Popen([sys.executable, str(script)], cwd=str(BASE))
    except OSError as exc:
        messagebox.showerror("启动失败", str(exc))


def main() -> None:
    window = tk.Tk()
    window.title("多功能计算器 · 课程项目")
    window.geometry("640x470")
    window.minsize(600, 440)
    try:
        window.iconbitmap(str(BASE / "play.ico"))
    except tk.TclError:
        pass

    frame = tk.Frame(window, padx=26, pady=20)
    frame.pack(fill="both", expand=True)

    tk.Label(
        frame,
        text="多功能计算器",
        font=("Microsoft YaHei", 22, "bold"),
        fg="#30475e",
    ).grid(row=0, column=0, columnspan=2, pady=(4, 2))

    tk.Label(
        frame,
        text="科学计算 · 进制转换 · 华容道 · 数独 · 2048",
        font=("Microsoft YaHei", 10),
        fg="#6b7785",
    ).grid(row=1, column=0, columnspan=2, pady=(0, 18))

    for index, (label, filename) in enumerate(MENU):
        button = tk.Button(
            frame,
            text=label,
            font=("Microsoft YaHei", 11),
            width=20,
            height=2,
            relief="groove",
            bg="#f7f8fa",
            activebackground="#e8eef4",
            command=lambda name=filename: launch(name),
        )
        button.grid(row=2 + index // 2, column=index % 2, padx=7, pady=6, sticky="nsew")

    tk.Button(
        frame,
        text="退出",
        font=("Microsoft YaHei", 10),
        command=window.destroy,
    ).grid(row=6, column=0, columnspan=2, pady=(16, 0))

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    window.mainloop()


if __name__ == "__main__":
    main()
