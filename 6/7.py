# 7. Симулятор магнитов и электромагнитов
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Магниты и электромагниты")
root.geometry("700x600")

fig, ax = plt.subplots(figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

magnets = []  # [(x,y,strength,pole), ...] pole: 'N' or 'S'
current_on = tk.BooleanVar(value=False)
I = tk.DoubleVar(value=1.0)


def add_magnet():
    x, y = float(entry_x.get()), float(entry_y.get())
    strength = float(entry_s.get())
    pole = 'N' if pole_var.get() == 0 else 'S'
    magnets.append([x, y, strength, pole])
    update_field()


def update_field():
    ax.clear()
    X, Y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
    U, V = np.zeros_like(X), np.zeros_like(Y)

    # Магнитные поля от постоянных магнитов
    for m in magnets:
        dx, dy = X - m[0], Y - m[1]
        r = np.sqrt(dx ** 2 + dy ** 2 + 0.1)
        B = m[2] / r ** 2
        U += B * np.cos(np.pi / 4 if m[3] == 'N' else -np.pi / 4) / r
        V += B * np.sin(np.pi / 4 if m[3] == 'N' else -np.pi / 4) / r

        color = 'red' if m[3] == 'N' else 'blue'
        ax.scatter(m[0], m[1], s=m[2] * 50, c=color, marker='^' if m[3] == 'N' else 'v')

    # Электромагнит в центре
    if current_on.get():
        B_center = I.get() * 0.1
