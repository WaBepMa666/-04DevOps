# 7. Панель с вводом пароля
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Авторизация")
root.geometry("300x200")

tk.Label(root, text="Календарь и погода", font=("Arial", 14)).pack(pady=20)

tk.Label(root, text="Пароль:").pack()
pwd_entry = tk.Entry(root, show="*", width=20)
pwd_entry.pack(pady=5)

def check_pwd():
    if pwd_entry.get() == "12345":
        messagebox.showinfo("Успех", "Доступ разрешен!\nПогода: +18°C ☀️")
    else:
        messagebox.showerror("Ошибка", "Неверный пароль")

tk.Button(root, text="Войти", command=check_pwd, bg="green", fg="white").pack(pady=20)
root.mainloop()
