# 1. Генератор файлов для осциллографа EWB
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

root = tk.Tk()
root.title("Генератор EWB осциллограф")
root.geometry("400x300")

dt = tk.DoubleVar(value=0.001)  # Шаг времени
bits_count = tk.IntVar(value=16)
duration = tk.DoubleVar(value=0.1)


def generate_ewb():
    t_step = dt.get()
    total_time = duration.get()
    n_points = int(total_time / t_step)

    # Генерация битов
    bits = np.random.randint(0, 2, bits_count.get())
    bit_duration = total_time / bits_count.get()

    # Создание сигнала
    time = np.linspace(0, total_time, n_points)
    voltage = np.zeros(n_points)

    for i, bit in enumerate(bits):
        start = int(i * bit_duration / t_step)
        end = int((i + 1) * bit_duration / t_step)
        voltage[start:end] = bit * 5.0

    # Сохранение файла
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text", "*.txt")])
    if filename:
        with open(filename, 'w') as f:
            f.write("Time\tV1\n")
            for t_val, v_val in zip(time, voltage):
                f.write(f"{t_val:.6f}\t{v_val:.1f}\n")
        messagebox.showinfo("Готово", f"Сохранено: {filename}")


tk.Label(root, text="Шаг времени (с):").pack()
tk.Entry(root, textvariable=dt).pack(pady=5)
tk.Label(root, text="Количество бит:").pack()
tk.Entry(root, textvariable=bits_count).pack(pady=5)
tk.Label(root, text="Длительность (с):").pack()
tk.Entry(root, textvariable=duration).pack(pady=5)

tk.Button(root, text="Генерировать EWB файл", command=generate_ewb,
          bg="lightgreen").pack(pady=20)
root.mainloop()
