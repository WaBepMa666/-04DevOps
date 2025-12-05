# 1. Панель управления машиностроительной установкой (Tkinter)
import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Панель управления установкой")
root.geometry("400x300")

status = tk.StringVar(value="Работает")
progress = tk.DoubleVar(value=65)
samples = tk.IntVar(value=12)
tests = tk.IntVar(value=8)

tk.Label(root, text="Статус:", font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=status, fg="green", font=("Arial", 14, "bold")).pack()

ttk.Progressbar(root, variable=progress, maximum=100).pack(pady=10, padx=20, fill="x")
tk.Label(root, text="Образцы: 12/20").pack()
tk.Label(root, text="Тесты: 8/15").pack()

btn_start = tk.Button(root, text="START", bg="green", fg="white")
btn_stop = tk.Button(root, text="STOP", bg="red", fg="white")
btn_start.pack(side="left", padx=20, pady=20)
btn_stop.pack(side="right", padx=20, pady=20)

def update_status():
    status.set(random.choice(["Работает", "Пауза", "Offline"]))
    progress.set(random.randint(0, 100))
    root.after(2000, update_status)

update_status()
root.mainloop()
