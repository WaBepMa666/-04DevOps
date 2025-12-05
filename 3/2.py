# 2. Выбор подключения к принтеру
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Подключение к принтеру")
root.geometry("350x250")

tk.Label(root, text="Выберите способ подключения:", font=("Arial", 12)).pack(pady=20)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=20, fill="both", expand=True)

wifi_frame = ttk.Frame(notebook)
printer_frame = ttk.Frame(notebook)
usb_frame = ttk.Frame(notebook)

notebook.add(wifi_frame, text="WiFi 📶")
notebook.add(printer_frame, text="Printer 🖨️")
notebook.add(usb_frame, text="USB 🔌")

tk.Label(printer_frame, text="Статус: Готов\nБумага: OK", font=("Arial", 11)).pack(pady=20)
tk.Button(printer_frame, text="Печать", bg="blue").pack(pady=10)

error_label = tk.Label(printer_frame, text="⚠️ Paper Jam", fg="orange", font=("Arial", 10))
error_label.pack(pady=5)

tk.Button(root, text="Подключиться", bg="green", fg="white").pack(pady=20)
root.mainloop()
