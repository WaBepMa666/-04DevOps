# 9. Графический калькулятор (Calculus Grapher)
import tkinter as tk
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Графический калькулятор")
root.geometry("700x500")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

expr_var = tk.StringVar(value="sin(x)")
x = sp.symbols('x')


def plot_function():
    try:
        expr = sp.sympify(expr_var.get())
        t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.vectorize(lambda ti: float(expr.subs(x, ti)))(t)

        # Производная
        deriv = sp.diff(expr, x)
        dy = np.vectorize(lambda ti: float(deriv.subs(x, ti)))(t)

        ax1.clear();
        ax1.plot(t, y, 'b-', label=f'f(x) = {expr_var.get()}')
        ax1.grid();
        ax1.legend()
        ax2.clear();
        ax2.plot(t, dy, 'r-', label=f"f'(x) = {sp.latex(deriv)}")
        ax2.grid();
        ax2.legend()
        canvas.draw()
    except:
        pass


tk.Label(root, "Функция f(x):").pack()
entry_func = tk.Entry(root, textvariable=expr_var, width=20)
entry_func.pack(pady=5)
tk.Button(root, text="Построить график", command=plot_function).pack(pady=5)
tk.Button(root, text="Примеры", command=lambda: expr_var.set("sin(x)+cos(x)")).pack()

plot_function()
root.mainloop()
