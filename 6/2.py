# 2. Симулятор электрического поля (Charges & Fields)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Электрическое поле")
root.geometry("700x600")

fig, ax = plt.subplots(figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

charges = []  # [(x, y, q), ...]


def add_charge():
    x = float(entry_x.get())
    y = float(entry_y.get())
    q = float(entry_q.get())
    charges.append((x, y, q))
    update_field()


def update_field():
    ax.clear()
    X, Y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
    U, V = np.zeros_like(X), np.zeros_like(Y)

    for i, (cx, cy, cq) in enumerate(charges):
        dx, dy = X - cx, Y - cy
        r = np.sqrt(dx ** 2 + dy ** 2 + 0.1)
        U += cq * dx / r ** 3
        V += cq * dy / r ** 3

        # Рисуем заряды
        color = 'red' if cq > 0 else 'blue'
        ax.scatter(cx, cy, s=abs(cq) * 100, c=color, marker='o')

    ax.quiver(X, Y, U, V, scale=50)
    ax.set_xlim(-5, 5);
    ax.set_ylim(-5, 5)
    ax.set_title("Векторное поле E");
    ax.grid()
    canvas.draw()


frame_ctrl = tk.Frame(root)
frame_ctrl.pack(side=tk.LEFT, padx=10)
tk.Label(frame_ctrl, text="x:").pack()
entry_x = tk.Entry(frame_ctrl);
entry_x.insert(0, "1");
entry_x.pack()
tk.Label(frame_ctrl, text="y:").pack()
entry_y = tk.Entry(frame_ctrl);
entry_y.insert(0, "1");
entry_y.pack()
tk.Label(frame_ctrl, text="q:").pack()
entry_q = tk.Entry(frame_ctrl);
entry_q.insert(0, "1");
entry_q.pack()
tk.Button(frame_ctrl, text="Добавить заряд", command=add_charge).pack(pady=10)
tk.Button(frame_ctrl, text="Очистить", command=lambda: [
global charges;
charges.clear();
update_field()]).pack()

update_field()
root.mainloop()
