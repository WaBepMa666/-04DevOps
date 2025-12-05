# 4. Гармонические колебания (амплитуда + частота)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Гармонические колебания")
root.geometry("600x500")

fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

frame_ctrl = tk.Frame(root)
frame_ctrl.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(frame_ctrl, text="Амплитуда:").pack()
amp_scale = tk.Scale(frame_ctrl, from_=0.5, to=3, resolution=0.1, orient=tk.HORIZONTAL)
amp_scale.set(1.0)
amp_scale.pack(pady=5)

tk.Label(frame_ctrl, text="Частота:").pack()
freq_scale = tk.Scale(frame_ctrl, from_=0.5, to=5, resolution=0.1, orient=tk.HORIZONTAL)
freq_scale.set(1.0)
freq_scale.pack(pady=5)


def update_plot():
    t = np.linspace(0, 4 * np.pi, 1000)
    A = amp_scale.get()
    f = freq_scale.get()
    y = A * np.sin(2 * np.pi * f * t)

    ax.clear()
    ax.plot(t, y, 'b-', linewidth=2)
    ax.set_title("y = A*sin(2πft)")
    ax.set_xlabel("Время");
    ax.set_ylabel("Амплитуда")
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-3.5, 3.5)
    canvas.draw()


def on_scale_change(*args):
    update_plot()


amp_scale.config(command=on_scale_change)
freq_scale.config(command=on_scale_change)
update_plot()
root.mainloop()
