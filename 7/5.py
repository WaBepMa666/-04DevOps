# 5. Сложение 5 синусоид
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Сложение 5 гармоник")
root.geometry("700x500")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

amps = [1.0, 0.7, 0.5, 0.3, 0.2]
freqs = [1, 2, 3, 4, 5]


def update_sum():
    t = np.linspace(0, 2 * np.pi, 2000)

    ax1.clear()
    for i in range(5):
        y = amps[i] * np.sin(2 * np.pi * freqs[i] * t)
        ax1.plot(t, y, label=f"f{i + 1}={freqs[i]}Hz")
    ax1.legend();
    ax1.set_title("Отдельные гармоники");
    ax1.grid()

    ax2.clear()
    y_sum = np.zeros_like(t)
    for i in range(5):
        y_sum += amps[i] * np.sin(2 * np.pi * freqs[i] * t)
    ax2.plot(t, y_sum, 'r-', linewidth=3, label="Сумма")
    ax2.set_title("Результат сложения");
    ax2.grid();
    ax2.legend()

    canvas.draw()


tk.Button(root, text="Обновить", command=update_sum).pack(pady=10)
update_sum()
root.mainloop()
