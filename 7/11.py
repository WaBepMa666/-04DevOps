# 11. PSK модуляция (Фазовая манипуляция)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("PSK Модуляция (BPSK)")
root.geometry("700x500")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

fc = tk.DoubleVar(value=12)
phase0 = tk.DoubleVar(value=0)
phase1 = tk.DoubleVar(value=np.pi)

frame_ctrl = tk.Frame(root)
frame_ctrl.pack(side=tk.LEFT, padx=10)

tk.Label(frame_ctrl, text="Несущая fc:").pack()
tk.Scale(frame_ctrl, from_=8, to=20, variable=fc, orient=tk.HORIZONTAL).pack(pady=2)
tk.Label(frame_ctrl, text="Фаза 0:").pack()
tk.Scale(frame_ctrl, from_=0, to=2 * np.pi, resolution=0.1, variable=phase0,
         orient=tk.HORIZONTAL).pack(pady=2)
tk.Label(frame_ctrl, text="Фаза 1:").pack()
tk.Scale(frame_ctrl, from_=0, to=2 * np.pi, resolution=0.1, variable=phase1,
         orient=tk.HORIZONTAL).pack(pady=2)


def update_psk():
    t = np.linspace(0, 2 * np.pi, 4000)
    bits = [0, 1, 0, 1, 1, 0, 0, 1]

    bit_dur = len(t) // len(bits)
    psk_signal = np.zeros_like(t)

    for i, bit in enumerate(bits):
        start = i * bit_dur
        end = start + bit_dur
        phase = phase0.get() if bit == 0 else phase1.get()
        psk_signal[start:end] = np.sin(2 * np.pi * fc.get() * t[start:end] + phase)

    ax1.clear();
    ax1.step(np.arange(len(bits)), bits);
    ax1.set_title("Биты");
    ax1.grid()
    ax2.clear();
    ax2.plot(t, psk_signal, 'g-', linewidth=2);
    ax2.set_title("BPSK");
    ax2.grid()
    canvas.draw()


def update(*args): update_psk()


fc.trace('w', update);
phase0.trace('w', update);
phase1.trace('w', update)
update_psk()
root.mainloop()
