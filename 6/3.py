# 3. Симулятор цепи (Battery-Resistor)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Battery-Resistor Circuit")
root.geometry("600x500")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

V = tk.DoubleVar(value=9.0)
R = tk.DoubleVar(value=1000.0)
f = tk.DoubleVar(value=1.0)


def update_circuit():
    t = np.linspace(0, 2 * np.pi / f.get(), 1000)
    I = V.get() / R.get() * np.sin(2 * np.pi * f.get() * t)
    P = V.get() * I

    ax1.clear();
    ax1.plot(t, I);
    ax1.set_title(f"I(t) = {V.get() / R.get():.3f} sin(2πft)")
    ax1.grid();
    ax1.set_ylabel("Ток, A")
    ax2.clear();
    ax2.plot(t, P);
    ax2.set_title("Мощность P(t)")
    ax2.grid();
    ax2.set_xlabel("Время");
    ax2.set_ylabel("P, Вт")
    canvas.draw()


tk.Label(root, text="Напряжение V:").pack()
tk.Scale(root, from_=1, to=15, variable=V, command=lambda x: update_circuit()).pack()
tk.Label(root, text="Сопротивление R:").pack()
tk.Scale(root, from_=100, to=5000, variable=R, command=lambda x: update_circuit()).pack()
tk.Label(root, text="Частота f:").pack()
tk.Scale(root, from_=0.5, to=5, variable=f, command=lambda x: update_circuit()).pack()

update_circuit()
root.mainloop()
