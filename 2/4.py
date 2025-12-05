import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


def update_display():
    """Обновляет отображаемое число по таймеру"""
    global current_number
    current_number = random.randint(0, max_range.get())
    number_label.config(text=f"Число: {current_number}")
    root.after(100, update_display)


def on_range_change(event):
    """Обработчик изменения TrackBar диапазона"""
    range_display.config(text=f"Диапазон: 0..{max_range.get()}")


def on_count_change(event):
    """Обработчик изменения TrackBar количества чисел"""
    count_display.config(text=f"Количество: {count_value.get()}")


def generate_numbers_graph():
    """Генерирует 1000 случайных чисел и выводит их графически как точки"""
    current_max = 100  # Фиксированный диапазон 0-100 для графика
    numbers = [random.randint(0, current_max) for _ in range(1000)]

    # Очищаем предыдущий график
    ax.clear()

    # Создаем точки: x - индекс, y - значение числа
    x = np.arange(1000)
    ax.scatter(x, numbers, s=1, alpha=0.6, color='blue')
    ax.set_title('1000 случайных чисел (0-100)')
    ax.set_xlabel('Индекс')
    ax.set_ylabel('Значение')
    ax.grid(True, alpha=0.3)

    # Автомасштабирование
    ax.set_ylim(0, 100)

    canvas.draw()


def generate_numbers_text():
    """Генерирует числа в текстовом поле"""
    memo.delete("1.0", "end")
    current_max = max_range.get()
    current_count = count_value.get()
    numbers = [random.randint(0, current_max) for _ in range(current_count)]
    memo.insert("1.0", "\n".join(map(str, numbers)))


# Создаем главное окно
root = tk.Tk()
root.title("Генератор случайных чисел с графиком")
root.geometry("1000x800")

# Создаем фигуру matplotlib
fig = Figure(figsize=(10, 5), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)

# TrackBar для диапазона (0-1000) - для текста
range_label = tk.Label(root, text="Диапазон для текста:", font=("Arial", 10, "bold"))
range_label.pack(pady=5)
max_range = tk.IntVar(value=100)
ttk.Scale(root, from_=0, to=1000, orient=tk.HORIZONTAL,
          variable=max_range, command=on_range_change,
          length=450).pack(pady=5)
range_display = tk.Label(root, text=f"Диапазон: 0..{max_range.get()}", font=("Arial", 11))
range_display.pack(pady=2)

# TrackBar для количества чисел (1-5000) - для текста
count_label_text = tk.Label(root, text="Количество для текста:", font=("Arial", 10, "bold"))
count_label_text.pack(pady=(20, 5))
count_value = tk.IntVar(value=1000)
ttk.Scale(root, from_=1, to=5000, orient=tk.HORIZONTAL,
          variable=count_value, command=on_count_change,
          length=450).pack(pady=5)
count_display = tk.Label(root, text=f"Количество: {count_value.get()}", font=("Arial", 11))
count_display.pack(pady=2)

# Отображение текущего числа
number_label = tk.Label(root, text="Число: --", font=("Arial", 16, "bold"),
                        fg="#2196F3", bg="#F5F5F5", relief=tk.RIDGE, padx=20, pady=10)
number_label.pack(pady=10)

# Кнопки
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_graph = tk.Button(btn_frame, text="График 1000 чисел (0-100)",
                      command=generate_numbers_graph, font=("Arial", 12),
                      bg="#FF9800", fg="white", width=22, height=2)
btn_graph.pack(side=tk.LEFT, padx=5)

btn_text = tk.Button(btn_frame, text="Текст чисел",
                     command=generate_numbers_text, font=("Arial", 12),
                     bg="#4CAF50", fg="white", width=15, height=2)
btn_text.pack(side=tk.LEFT, padx=5)

# Переменная для текущего числа
current_number = 0

# Запускаем таймер
update_display()

root.mainloop()
