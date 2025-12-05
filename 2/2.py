import tkinter as tk
from tkinter import ttk
import random

def update_display():
    """Обновляет отображаемое число по таймеру"""
    global current_number
    current_number = random.randint(0, max_value.get())
    number_label.config(text=f"Число: {current_number}")
    root.after(100, update_display)  # Обновление каждые 100мс

def on_trackbar_change(event):
    """Обработчик изменения TrackBar"""
    global max_value
    max_label.config(text=f"Диапазон: 0..{max_value.get()}")
    # Немедленно обновляем число при ручном изменении
    current_number = random.randint(0, max_value.get())
    number_label.config(text=f"Число: {current_number}")

def generate_numbers():
    """Генерирует 1000 чисел в диапазоне TrackBar"""
    memo.delete("1.0", "end")
    current_max = max_value.get()
    numbers = [random.randint(0, current_max) for _ in range(1000)]
    memo.insert("1.0", "\n".join(map(str, numbers)))

# Создаем главное окно
root = tk.Tk()
root.title("Генератор случайных чисел с TrackBar")
root.geometry("500x700")

# Переменная для максимального значения TrackBar
max_value = tk.IntVar(value=100)

# TrackBar (Scale)
trackbar_label = tk.Label(root, text="Диапазон случайных чисел:", font=("Arial", 10, "bold"))
trackbar_label.pack(pady=5)

ttk.Scale(root, from_=0, to=1000, orient=tk.HORIZONTAL,
          variable=max_value, command=on_trackbar_change,
          length=400).pack(pady=5)

max_label = tk.Label(root, text=f"Диапазон: 0..{max_value.get()}", font=("Arial", 11))
max_label.pack(pady=5)

# Отображение текущего числа (меняется по таймеру)
number_label = tk.Label(root, text="Число: --", font=("Arial", 16, "bold"),
                       fg="#2196F3", bg="#F5F5F5")
number_label.pack(pady=20)

# Поле Memo
memo_label = tk.Label(root, text="1000 случайных чисел:", font=("Arial", 10, "bold"))
memo_label.pack(anchor="w", padx=10)
memo = tk.Text(root, height=25, width=60, wrap=tk.NONE)
memo.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# Кнопка генерации
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_generate = tk.Button(btn_frame, text="Сгенерировать 1000 чисел",
                        command=generate_numbers, font=("Arial", 12),
                        bg="#4CAF50", fg="white", width=20)
btn_generate.pack(side=tk.LEFT, padx=5)

# Переменная для текущего числа
current_number = 0

# Запускаем таймер обновления
update_display()

root.mainloop()
