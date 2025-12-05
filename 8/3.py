# 3. Генератор текстовых файлов + sin/cos
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

root = tk.Tk()
root.title("Генератор файлов")
root.geometry("400x350")

text_content = tk.StringVar(value="Пример текста\nСлучайные данные")
n_random = tk.IntVar(value=20)
function_type = tk.StringVar(value="sin")


def generate_text_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text_content.get() + "\n\n")

            # Случайные числа
            f.write("Случайные числа:\n")
            for i in range(n_random.get()):
                f.write(f"{random.randint(0, 1000)} ")
            f.write("\n\n")

            # Математическая функция
            t = np.linspace(0, 2 * np.pi, 50)
            func = np.sin if function_type.get() == "sin" else np.cos
            f.write("sin/cos значения:\n")
            for ti, yi in zip(t, func(t)):
                f.write(f"t={ti:.2f}: {yi:.3f}\n")

        messagebox.showinfo("Готово", f"Файл сохранен: {filename}")


tk.Label(root, "Текст:").pack()
tk.Text(root, height=4, width=40, textvariable=text_content).pack(pady=5)
tk.Label(root, "Случайных чисел:").pack()
tk.Entry(root, textvariable=n_random).pack(pady=5)
tk.Label(root, "Функция:").pack()
tk.OptionMenu(root, function_type, "sin", "cos").pack(pady=5)
tk.Button(root, text="Создать файл", command=generate_text_file).pack(pady=20)
root.mainloop()
