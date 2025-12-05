# 5. Мониторинг тестов (6 карточек)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Мониторинг процессов")
root.geometry("450x400")

tk.Label(root, text="Дашборд мониторинга", font=("Arial", 16, "bold")).pack(pady=10)

cards = [
    ("Tests in Process", "20", "lightblue"),
    ("QC", "75%", "lightgreen"),
    ("Reagents", "👍", "lime"),
    ("Calibration", "⚠️", "yellow"),
    ("Supplies", "⚠️", "orange"),
    ("Process Path", "➡️➡️", "lightgray")
]

for i, (title, value, color) in enumerate(cards):
    frame = tk.Frame(root, bg=color, relief="raised", bd=2)
    frame.pack(fill="x", padx=20, pady=5)
    tk.Label(frame, text=title, font=("Arial", 10, "bold"), bg=color).pack()
    tk.Label(frame, text=value, font=("Arial", 14), bg=color).pack(pady=5)

root.mainloop()
