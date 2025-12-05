# 4. Календарь с погодой
import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("Календарь + Погода")
root.geometry("300x250")

today = datetime.now().strftime("%d.%m.%Y")
tk.Label(root, text=f"Сегодня: {today}", font=("Arial", 14)).pack(pady=10)

cal = ttk.Calendar(root, selectmode="day")
cal.pack(pady=10)

weather = tk.Label(root, text="🌤️ +18°C\nЯсно", font=("Arial", 12), bg="lightblue")
weather.pack(pady=10)

tk.Label(root, text="Введите пароль для доступа:", font=("Arial", 10)).pack(pady=(20,5))
entry = tk.Entry(root, show="*", width=15)
entry.pack()
tk.Button(root, text="Войти").pack(pady=5)

root.mainloop()
