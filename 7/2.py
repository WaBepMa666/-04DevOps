# 2. Кодировщик сигналов (NRZ, Manchester, MLT-3, AMI)
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.title("Кодировщики сигналов")
root.geometry("800x500")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

bits = [0, 1, 1, 0, 0, 1, 0, 1]


def encode_nrz(bits):
    t = np.linspace(0, len(bits), 1000)
    signal = np.repeat(bits, 125)
    return t[:len(signal)], signal


def encode_manchester(bits):
    t, signal = [], []
    for bit in bits:
        t.extend(np.linspace(0, 1, 500))
        signal.extend([0] * 250 + [1] * 250 if bit else [1] * 250 + [0] * 250)
    return np.array(t), np.array(signal)


def plot_encoding():
    ax1.clear();
    ax2.clear()

    t_nrz, s_nrz = encode_nrz(bits)
    ax1.plot(t_nrz, s_nrz, 'b-', linewidth=2);
    ax1.set_title("NRZ");
    ax1.grid()

    t_man, s_man = encode_manchester(bits)
    ax2.plot(t_man, s_man, 'r-', linewidth=2);
    ax2.set_title("Manchester");
    ax2.grid()

    canvas.draw()


entry_bits = tk.Entry(root, width=20)
entry_bits.insert(0, "01100101")
entry_bits.pack(pady=5)


def update_bits():
    global bits
    bits = [int(c) for c in entry_bits.get() if c in '01']
    plot_encoding()


tk.Button(root, text="Обновить", command=update_bits).pack()
plot_encoding()
root.mainloop()
