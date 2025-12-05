# 6. Амплитудная модуляция (AM)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Амплитудная модуляция")
root.geometry("700x500")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

fc = tk.DoubleVar(value=10)  # Несущая частота
Am = tk.DoubleVar(value=1.0)  # Амплитуда несущей
m = tk.DoubleVar(value=0.5)  # Глубина модуляции
fm = tk.DoubleVar(value=1)  # Частота модуляции

frame_ctrl = tk.Frame(root)
frame_ctrl.pack(side=tk.LEFT, padx=10)

tk.Label(frame_ctrl, text="fc (несущая):").pack()
tk.Scale(frame_ctrl, from_=5, to=20, resolution=0.5, orient=tk.HORIZONTAL,
         variable=fc).pack(pady=2)
tk.Label(frame_ctrl, text="Глубина m:").pack()
tk.Scale(frame_ctrl, from_=0, to=1, resolution=0.05, orient=tk.HORIZONTAL,
         variable=m).pack(pady=2)


def update_am():
    t = np.linspace(0, 2 * np.pi, 4000)
    mod_signal = (1 + m.get() * np.sin(2 * np.pi * fm.get() * t))
    carrier = Am.get() * np.sin(2 * np.pi * fc.get() * t)
    am_signal = mod_signal * carrier

    ax1.clear();
    ax1.plot(t, mod_signal);
    ax1.set_title("Модулирующий сигнал")
    ax2.clear();
    ax2.plot(t, carrier);
    ax2.set_title("Несущая")
    ax3.clear();
    ax3.plot(t, am_signal, 'r-', linewidth=2);
    ax3.set_title("AM сигнал")
    for ax in [ax1, ax2, ax3]: ax.grid()
    canvas.draw()


def update(*args): update_am()


fc.trace('w', update);
m.trace('w', update)
update_am()
root.mainloop()
