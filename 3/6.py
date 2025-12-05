# 6. Сетка мониторинга (2x3)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x300")
root.title("Сетка мониторинга")

header = tk.Label(root, text="Техническое обслуживание", font=("Arial", 16))
header.pack(pady=10)

grid = tk.Frame(root)
grid.pack(pady=20)

labels = [
    ("Tests\n20", "lightblue"), ("QC\n📊", "green"),
    ("Reagents\n👍", "lime"), ("Calibration\n⚠️", "yellow"),
    ("Supplies\n⚠️", "orange"), ("Path\n➡️", "gray")
]

for i, (text, color) in enumerate(labels):
    row, col = divmod(i, 2)
    card = tk.Label(grid, text=text, bg=color, fg="black",
                   font=("Arial", 12, "bold"), width=15, height=4,
                   relief="raised", bd=2)
    card.grid(row=row, column=col, padx=10, pady=10)

tk.Button(root, text="Обновить").pack(pady=10)
root.mainloop()
