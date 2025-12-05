# 3. Планировщик техобслуживания
import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("Техобслуживание")
root.geometry("400x350")

header = tk.Label(root, text="Статус процессов", font=("Arial", 14, "bold"))
header.pack(pady=10)

grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)

tests_label = tk.Label(grid_frame, text="Tests in Process\n20", bg="lightblue")
tests_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

qc_prog = ttk.Progressbar(grid_frame, value=75, length=100)
qc_prog.grid(row=0, column=1, padx=10, pady=10)

tk.Label(grid_frame, text="Reagents\n👍", bg="lightgreen").grid(row=1, column=0)
tk.Label(grid_frame, text="Calibration\n⚠️", bg="yellow").grid(row=1, column=1)
tk.Label(grid_frame, text="Supplies\n⚠️", bg="orange").grid(row=2, column=0)
tk.Label(grid_frame, text="Process Path\n➡️", bg="lightgray").grid(row=2, column=1)

tk.Button(root, text="Обновить статус").pack(pady=10)
root.mainloop()
