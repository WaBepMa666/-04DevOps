# 4. Физический движок (твердые частицы)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

root = tk.Tk()
root.title("Физический движок")
root.geometry("700x500")

fig, ax = plt.subplots(figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

particles = []  # [(x,y,vx,vy,m), ...]
dt = 0.05
G = 100


def add_particle():
    x, y = np.random.uniform(-4, 4, 2)
    vx, vy = np.random.uniform(-1, 1, 2)
    m = random.uniform(0.1, 1)
    particles.append([x, y, vx, vy, m])
    animate(None)


def update_physics(frame):
    ax.clear()
    for i, p in enumerate(particles):
        for j, q in enumerate(particles):
            if i != j:
                dx, dy = q[0] - p[0], q[1] - p[1]
                r = np.sqrt(dx ** 2 + dy ** 2) + 0.1
                f = G * p[4] * q[4] / r ** 2
                p[2] += f * dx / r * dt / p[4]  # ax
                p[3] += f * dy / r * dt / p[4]  # ay

        p[0] += p[2] * dt  # x
        p[1] += p[3] * dt  # y

        ax.scatter(p[0], p[1], s=p[4] * 100, c='red', alpha=0.7)

    ax.set_xlim(-5, 5);
    ax.set_ylim(-5, 5);
    ax.grid()
    canvas.draw()


tk.Button(root, text="Добавить частицы", command=lambda: [add_particle() for _ in range(3)]).pack()
tk.Button(root, text="Очистить", command=lambda: [
global particles;
particles.clear()]).pack()

ani = FuncAnimation(fig, update_physics, interval=50, blit=False)
root.mainloop()
