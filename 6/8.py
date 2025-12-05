# 8. Конструктор цепей переменного тока
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Конструктор цепей AC")
root.geometry("800x600")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Параметры элементов
R = tk.DoubleVar(value=100)
L = tk.DoubleVar(value=0.1)
C = tk.DoubleVar(value=1e-6)
f = tk.DoubleVar(value=50)


def update_circuit():
    omega = 2 * np.pi * f.get()
    Z_R = R.get()
    Z_L = 1j * omega * L.get()
    Z_C = 1j / (omega * C.get())
    Z_total = Z_R + Z_L + Z_C

    t = np.linspace(0, 0.1, 1000)
    V_in = 220 * np.sin(omega * t)
    I = V_in / np.abs(Z_total)

    ax1.clear();
    ax1.plot(t * 1000, V_in, label='Напряжение');
    ax1.plot(t * 1000, I.real, label='Ток')
    ax1.set_xlabel('Время, мс');
    ax1.legend();
    ax1.grid()

    ax2.clear()
    ax2.bar(['R', 'L', 'C', 'Σ'], [np.abs(Z_R), np.abs(Z_L), np.abs(Z_C), np.abs(Z_total)])
    ax2.set_ylabel('|Z|, Ом');
    ax2.set_title('Импедансы')
    canvas.draw()


frame_ctrl = tk.Frame(root)
frame_ctrl.pack(side=tk.LEFT, padx=10)
tk.Label(frame_ctrl, "R, Ом:").pack()
tk.Scale(frame_ctrl, from_=10, to=1000, variable=R, command=lambda x: update_circuit()).pack()
tk.Label(frame_ctrl, "L, Гн:").pack()
tk.Scale(frame_ctrl, from_=0.01, to=1, variable=L, command=lambda x: update_circuit()).pack()
tk.Label(frame_ctrl, "C, Ф:").pack()
tk.Scale(frame_ctrl, from_=1e-7, to=1e-4, variable=C, command=lambda x: update_circuit()).pack()
tk.Label(frame_ctrl, "f, Гц:").pack()
tk.Scale(frame_ctrl, from_=10, to=1000, variable=f, command=lambda x: update_circuit()).pack()

update_circuit()
root.mainloop()
