# 5. Отправка данных через каналы связи
import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MimeText
import webbrowser

root = tk.Tk()
root.title("Отправка данных")
root.geometry("400x300")

message_text = tk.StringVar(value="Тестовое сообщение")
recipient = tk.StringVar(value="test@example.com")


def send_email():
    try:
        msg = MimeText(message_text.get())
        msg['Subject'] = 'Данные с Python'
        msg['From'] = 'test@python.local'
        msg['To'] = recipient.get()

        # Для демо - открываем почтовый клиент
        webbrowser.open(f"mailto:{recipient.get()}?subject=Данные&body={message_text.get()}")
        messagebox.showinfo("Готово", "Почтовый клиент открыт!")
    except:
        messagebox.showerror("Ошибка", "Не удалось отправить")


def send_sms_demo():
    webbrowser.open("https://web.telegram.org")
    messagebox.showinfo("SMS", "Откройте Telegram Web для отправки")


tk.Label(root, "Сообщение:").pack()
tk.Text(root, height=6, width=40, textvariable=message_text).pack(pady=5)
tk.Label(root, "Получатель:").pack()
tk.Entry(root, textvariable=recipient, width=30).pack(pady=5)

tk.Button(root, text="📧 Email", command=send_email, bg="lightblue").pack(pady=5)
tk.Button(root, text="📱 SMS/Telegram", command=sms_demo, bg="lightgreen").pack(pady=5)
tk.Button(root, text="📊 Push API", command=lambda: webbrowser.open("https://onesignal.com"),
          bg="orange").pack(pady=5)
root.mainloop()
