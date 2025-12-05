# 12. Модель твердых тел (физический движок 2D)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches

root = tk.Tk()
root.title("Динамика твердых тел")
root.geometry("700x500")

fig, ax = plt.subplots(figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

bodies = []  # [x, y, vx, vy, angle, omega, size]
G = 500
dt = 0.02


def add_body():
    x, y = np.random.uniform(-3, 3, 2)
    bodies.append([x, y, 0, 0, 0, 0, np.random.uniform(0.3, 0.8)])
    update_physics()


def update_physics():
    ax.clear()
    for i, b in enumerate(bodies):
        for j, other in enumerate(bodies):
            if i != j:
                dx, dy = other[0] - b[0], other[1] - b[1]
                r = np.sqrt(dx ** 2 + dy ** 2)
                if r > 0.1:
                    force = G / r ** 2
                    b[2] += force * dx / r * dt / 0.5  # ускорение
                    b[3] += force * dy / r * dt / 0.5
                    b[5] += np.random.uniform(-0.1, 0.1)  # вращение

        # Интеграция
        b[0] += b[2] * dt
        b[1] += b[3] * dt
        b[4] += b[5] * dt

        # Отрисовка
        rect = patches.Rectangle((b[0] - b[6] / 2, b[1] - b[6] / 2), b[6], b[6],
                                 angle=np.degrees(b[4]), alpha=0.7)
        ax.add_patch(rect)

    ax.set_xlim(-5, 5);
    ax.set_ylim(-5, 5);
    ax.grid()
    ax.set_title("Динамика твердых тел")
    canvas.draw()


tk.Button(root, text="Добавить тела (5)",
          command=lambda: [add_body() for _ in range(5)]).pack(pady=10)
tk.Button(root, text="Очистить",
          command=lambda: [
global bodies;
bodies.clear();
update_physics()]).pack()

add_body()
update_physics()
root.mainloop()
