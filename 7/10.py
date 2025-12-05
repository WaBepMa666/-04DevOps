# 10. ASK модуляция (Амплитудная ключевая)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("ASK Модуляция")
root.geometry("700x500")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

fc = tk.DoubleVar(value=15)  # Несущая частота
A0 = tk.DoubleVar(value=0.0)  # Амплитуда для 0
A1 = tk.DoubleVar(value=1.0)  # Амплитуда для 1

frame_ctrl = tk.Frame(root)
frame_ctrl.pack(side=tk.LEFT, padx=10)

tk.Label(frame_ctrl, text="Несущая fс:").pack()
tk.Scale(frame_ctrl, from_=10, to=30, resolution=1, variable=fc,
         orient=tk.HORIZONTAL).pack(pady=2)
tk.Label(frame_ctrl, text="A0 (для 0):").pack()
tk.Scale(frame_ctrl, from_=0, to=0.5, resolution=0.05, variable=A0,
         orient=tk.HORIZONTAL).pack(pady=2)
tk.Label(frame_ctrl, text="A1 (для 1):").pack()
tk.Scale(frame_ctrl, from_=0.5, to=2, resolution=0.05, variable=A1,
         orient=tk.HORIZONTAL).pack(pady=2)


def update_ask():
    t = np.linspace(0, 2 * np.pi, 5000)
    bits = [0, 1, 1, 0, 1, 0, 0, 1]

    bit_dur = len(t) // len(bits)
    ask_signal = np.zeros_like(t)

    for i, bit in enumerate(bits):
        start = i * bit_dur
        end = start + bit_dur
        amp = A0.get() if bit == 0 else A1.get()
        ask_signal[start:end] = amp * np.sin(2 * np.pi * fc.get() * t[start:end])

    ax1.clear();
    ax1.step(np.arange(len(bits)), bits, where='mid');
    ax1.set_title("Биты")
    ax2.clear();
    ax2.plot(t[:bit_dur * 2], ask_signal[:bit_dur * 2]);
    ax2.set_title("ASK сигнал")
    ax3.clear();
    ax3.plot(t[:bit_dur * 4], ask_signal[:bit_dur * 4]);
    ax3.set_title("Полный сигнал")
    for ax in [ax1, ax2, ax3]: ax.grid()
    canvas.draw()


def update(*args): update_ask()


fc.trace('w', update);
A0.trace('w', update);
A1.trace('w', update)
update_ask()
root.mainloop()
