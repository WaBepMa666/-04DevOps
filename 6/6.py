# 6. 3D график комплексного синуса
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("3D Комплексный синус")
root.geometry("700x600")

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def update_3d():
    ax.clear()
    theta = np.linspace(0, 4 * np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 50)
    T, P = np.meshgrid(theta, phi)

    X = np.cos(T) * np.sin(P)
    Y = np.sin(T) * np.sin(P)
    Z = np.cos(P)

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('X');
    ax.set_ylabel('Y');
    ax.set_zlabel('Z')
    ax.set_title('Функция синуса в комплексной плоскости')
    canvas.draw()


tk.Scale(root, from_=0.1, to=2, orient=tk.HORIZONTAL, label="Масштаб").pack()
tk.Button(root, text="Обновить 3D", command=update_3d).pack(pady=10)

update_3d()
root.mainloop()
