import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# Главное окно ПЕРВЫМ
root = tk.Tk()
root.title("Генератор случайных чисел")
root.geometry("1400x900")
root.minsize(1200, 800)

# Переменные ПОСЛЕ root
graph_range = tk.IntVar(value=100)
graph_count = tk.IntVar(value=1000)
max_range = tk.IntVar(value=100)
count_value = tk.IntVar(value=1000)
current_number = 0


def update_display():
    global current_number
    current_number = random.randint(0, max_range.get())
    number_label.config(text=f"Число: {current_number}")
    root.after(100, update_display)


def generate_graph():
    count = graph_count.get()
    max_val = graph_range.get()
    numbers = [random.randint(0, max_val) for _ in range(count)]
    x = np.arange(count)

    ax.clear()
    ax.scatter(x, numbers, s=3, alpha=0.7, color='blue')
    ax.set_title(f'{count} случайных чисел (0-{max_val})')
    ax.set_xlabel('Индекс')
    ax.set_ylabel('Значение')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, max_val + 10)
    canvas.draw()
    status_label.config(text=f"График: {count} точек (0-{max_val})")


def generate_text():
    memo.delete("1.0", "end")
    numbers = [random.randint(0, max_range.get()) for _ in range(count_value.get())]
    memo.insert("1.0", "\n".join(map(str, numbers)))
    status_label.config(text=f"Текст: {count_value.get()} чисел (0-{max_range.get()})")


def clear_all():
    ax.clear()
    canvas.draw()
    memo.delete("1.0", "end")
    status_label.config(text="Очищено")


def save_graph():
    fig.savefig("график.png", dpi=300, bbox_inches='tight')
    status_label.config(text="График сохранен: график.png")


# Стиль кнопок
style = ttk.Style()
style.configure('Big.TButton', font=('Arial', 14, 'bold'), padding=20)

# График
fig = Figure(figsize=(12, 6), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)

# Панель управления
control_frame = ttk.LabelFrame(root, text="Настройки", padding=10)
control_frame.pack(pady=10, fill=tk.X, padx=10)

# График настройки
ttk.Label(control_frame, text="График диапазон:", font=('Arial', 12)).grid(row=0, column=0, sticky='w', padx=5)
ttk.Scale(control_frame, from_=0, to=100, variable=graph_range, orient=tk.HORIZONTAL, length=200).grid(row=0, column=1,
                                                                                                       padx=5)
ttk.Label(control_frame, textvariable=graph_range).grid(row=0, column=2, padx=5)

ttk.Scale(control_frame, from_=1, to=1000, variable=graph_count, orient=tk.HORIZONTAL, length=200).grid(row=0, column=3,
                                                                                                        padx=5)
ttk.Label(control_frame, textvariable=graph_count).grid(row=0, column=4, padx=5)

# Текст настройки
ttk.Label(control_frame, text="Текст диапазон:", font=('Arial', 12)).grid(row=1, column=0, sticky='w', pady=(15, 0),
                                                                          padx=5)
ttk.Scale(control_frame, from_=0, to=1000, variable=max_range, orient=tk.HORIZONTAL, length=200).grid(row=1, column=1,
                                                                                                      pady=(15, 0),
                                                                                                      padx=5)
ttk.Label(control_frame, textvariable=max_range).grid(row=1, column=2, pady=(15, 0), padx=5)

ttk.Scale(control_frame, from_=1, to=5000, variable=count_value, orient=tk.HORIZONTAL, length=200).grid(row=1, column=3,
                                                                                                        pady=(15, 0),
                                                                                                        padx=5)
ttk.Label(control_frame, textvariable=count_value).grid(row=1, column=4, pady=(15, 0), padx=5)

# КНОПКИ
button_frame = ttk.Frame(root)
button_frame.pack(pady=20, fill=tk.X, padx=20)

ttk.Button(button_frame, text="📊 График", command=generate_graph, style='Big.TButton').pack(side=tk.LEFT, padx=10,
                                                                                            pady=10)
ttk.Button(button_frame, text="📝 Текст", command=generate_text, style='Big.TButton').pack(side=tk.LEFT, padx=10,
                                                                                          pady=10)
ttk.Button(button_frame, text="🗑️ Очистить", command=clear_all, style='Big.TButton').pack(side=tk.LEFT, padx=10,
                                                                                          pady=10)
ttk.Button(button_frame, text="💾 Сохранить", command=save_graph, style='Big.TButton').pack(side=tk.RIGHT, padx=10,
                                                                                           pady=10)

# Статус и число
status_label = ttk.Label(root, text="Готов к работе", font=('Arial', 12))
status_label.pack(pady=5)

number_label = ttk.Label(root, text="Число: --", font=('Arial', 18, 'bold'))
number_label.pack(pady=10)

# Текстовое поле
memo = tk.Text(root, height=10, font=("Consolas", 11), wrap=tk.NONE)
memo.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Запуск
update_display()
root.mainloop()
