# 8. Комплексный дашборд
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Управление установкой")
root.geometry("450x350")

# Верхняя панель статуса
status_frame = tk.Frame(root, bg="lightgray")
status_frame.pack(fill="x", pady=5)
tk.Label(status_frame, text="🟢 РАБОТАЕТ | Образцы: 12/20 | Тесты: 8/15",
         bg="lightgray", font=("Arial", 11)).pack()

# Карточки 2x3
grid = ttk.Frame(root)
grid.pack(pady=10)

cards_data = [("Tests", "20"), ("QC", "75%"), ("Reagents", "OK"),
              ("Calib", "⚠️"), ("Supplies", "LOW"), ("Path", "Active")]

for i, (title, status) in enumerate(cards_data):
    row, col = divmod(i, 2)
    card = tk.Label(grid, text=f"{title}\n{status}", relief="solid",
                   width=12, height=4, font=("Arial", 10))
    card.grid(row=row, column=col, padx=8, pady=8)

# Управление
ctrl_frame = tk.Frame(root)
ctrl_frame.pack(pady=20)
tk.Button(ctrl_frame, text="START", bg="green", fg="white").pack(side="left", padx=20)
tk.Button(ctrl_frame, text="STOP", bg="red", fg="white").pack(side="left", padx=20)
tk.Button(ctrl_frame, text="Сброс", bg="orange").pack(side="left", padx=20)

root.mainloop()
