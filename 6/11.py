# 11. Симулятор движения частиц в средах (металл/электролит/газ)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

root = tk.Tk()
root.title("Движение частиц в средах")
root.geometry("700x500")

fig, ax = plt.subplots(figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

particles = np.array([[np.random.uniform(-4, 4), np.random.uniform(-2, 2),
                       np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5)]
                      for _ in range(20)])
medium = tk.StringVar(value="Металл")
dt = 0.05


def update_particles(frame):
    ax.clear()
    global particles

    if medium.get() == "Металл":
        friction = 0.9
        field = 0.1
    elif medium.get() == "Электролит":
        friction = 0.7
        field = 0.05
    else:  # Газ
        friction = 0.95
        field = 0.02

    # Электрическое поле + трение
    particles[:, 2] *= friction  # vx *= friction
    particles[:, 3] *= friction  # vy *= friction
    particles[:, 2] += field  # E-поле по x
    particles[:, 0] += particles[:, 2] * dt
    particles[:, 1] += particles[:, 3] * dt

    # Границы
    particles[:, 0] = np.clip(particles[:, 0], -4.5, 4.5)

    scatter = ax.scatter(particles[:, 0], particles[:, 1],
                         s=50, c=particles[:, 2], cmap='plasma')
    ax.set_xlim(-5, 5);
    ax.set_ylim(-3, 3);
    ax.grid()
    ax.set_title(f"Движение в {medium.get()}")
    plt.colorbar(scatter, label="Скорость Vx")
    canvas.draw()


tk.Label(root, text="Среда:").pack()
for med in ["Металл", "Электролит", "Газ"]:
    tk.Radiobutton(root, text=med, variable=medium,
                   value=med, command=lambda: ani.event_source.stop()).pack()

ani = animation.FuncAnimation(fig, update_particles, interval=50, cache_frame_data=False)
root.mainloop()
