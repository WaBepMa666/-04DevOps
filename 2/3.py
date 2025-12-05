import tkinter as tk
from tkinter import ttk
import random

def update_display():
    """Обновляет отображаемое число по таймеру"""
    global current_number
    current_number = random.randint(0, max_range.get())  # Исправлено: max_range вместо max_value
    number_label.config(text=f"Число: {current_number}")
    root.after(100, update_display)

def on_range_change(event):
    """Обработчик изменения TrackBar диапазона"""
    range_display.config(text=f"Диапазон: 0..{max_range.get()}")

def on_count_change(event):
    """Обработчик изменения TrackBar количества чисел"""
    count_display.config(text=f"Количество: {count_value.get()}")

def generate_numbers():
    """Генерирует указанное количество чисел в диапазоне"""
    memo.delete("1.0", "end")
    current_max = max_range.get()
    current_count = count_value.get()
    numbers = [random.randint(0, current_max) for _ in range(current_count)]
    memo.insert("1.0", "\n".join(map(str, numbers)))

# Создаем главное окно
root = tk.Tk()
root.title("Генератор случайных чисел с TrackBar")
root.geometry("550x750")

# TrackBar для диапазона (0-1000)
range_label = tk.Label(root, text="Диапазон случайных чисел:", font=("Arial", 10, "bold"))
range_label.pack(pady=5)
max_range = tk.IntVar(value=100)

ttk.Scale(root, from_=0, to=1000, orient=tk.HORIZONTAL,
          variable=max_range, command=on_range_change,
          length=450).pack(pady=5)
range_display = tk.Label(root, text=f"Диапазон: 0..{max_range.get()}", font=("Arial", 11))
range_display.pack(pady=2)

# TrackBar для количества чисел (1-5000)
count_label_text = tk.Label(root, text="Количество чисел:", font=("Arial", 10, "bold"))
count_label_text.pack(pady=(20,5))
count_value = tk.IntVar(value=1000)

ttk.Scale(root, from_=1, to=5000, orient=tk.HORIZONTAL,
          variable=count_value, command=on_count_change,
          length=450).pack(pady=5)
count_display = tk.Label(root, text=f"Количество: {count_value.get()}", font=("Arial", 11))
count_display.pack(pady=2)

# Отображение текущего числа
number_label = tk.Label(root, text="Число: --", font=("Arial", 16, "bold"),
                       fg="#2196F3", bg="#F5F5F5", relief=tk.RIDGE, padx=20, pady=10)
number_label.pack(pady=20)

# Поле Memo
memo_label = tk.Label(root, text="Случайные числа:", font=("Arial", 10, "bold"))
memo_label.pack(anchor="w", padx=10)
memo = tk.Text(root, height=25, width=65, wrap=tk.NONE)
memo.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# Кнопка генерации
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_generate = tk.Button(btn_frame, text="Сгенерировать числа",
                        command=generate_numbers, font=("Arial", 12),
                        bg="#4CAF50", fg="white", width=20, height=2)
btn_generate.pack(side=tk.LEFT, padx=5)

# Переменная для текущего числа
current_number = 0

# Запускаем таймер
update_display()

root.mainloop()
