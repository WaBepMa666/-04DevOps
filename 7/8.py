# 8. FSK модуляция (Частотная манипуляция)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("FSK Модуляция")
root.geometry("700x500")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

f0 = tk.DoubleVar(value=10)  # Частота для 0
f1 = tk.DoubleVar(value=15)  # Частота для 1
A = tk.DoubleVar(value=1.0)  # Амплитуда

frame_ctrl = tk.Frame(root)
frame_ctrl.pack(side=tk.LEFT, padx=10)

tk.Label(frame_ctrl, text="f0 (для 0):").pack()
tk.Scale(frame_ctrl, from_=5, to=20, resolution=0.5, variable=f0,
         orient=tk.HORIZONTAL).pack(pady=2)
tk.Label(frame_ctrl, text="f1 (для 1):").pack()
tk.Scale(frame_ctrl, from_=10, to=25, resolution=0.5, variable=f1,
         orient=tk.HORIZONTAL).pack(pady=2)


def update_fsk():
    t = np.linspace(0, 2 * np.pi, 4000)
    bits = [0, 1, 1, 0, 0, 1, 0, 1]
    fsk_signal = np.zeros_like(t)

    bit_dur = len(t) // len(bits)
    for i, bit in enumerate(bits):
        freq = f0.get() if bit == 0 else f1.get()
        start = i * bit_dur
        end = start + bit_dur
        fsk_signal[start:end] = A.get() * np.sin(2 * np.pi * freq * t[start:end])

    ax1.clear();
    ax1.plot(t[:bit_dur * 2], fsk_signal[:bit_dur * 2]);
    ax1.set_title("FSK сигнал")
    ax1.grid()
    bits_t = np.repeat(bits, bit_dur)
    ax2.clear();
    ax2.plot(t[:len(bits_t)], bits_t, 'r-');
    ax2.set_title("Исходные биты")
    ax2.grid()
    canvas.draw()


def update(*args): update_fsk()


f0.trace('w', update);
f1.trace('w', update)
update_fsk()
root.mainloop()
