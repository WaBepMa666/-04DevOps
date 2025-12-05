# 10. Тепловые карты и области (Meteorological data)
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Тепловые карты")
root.geometry("700x600")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

temp_data = np.random.rand(20, 20) * 30
traffic_data = np.random.rand(15, 15) * 100


def update_maps():
    # Температура
    im1 = ax1.imshow(temp_data, cmap='hot', vmin=0, vmax=30)
    ax1.set_title("Температура °C")

    # Трафик
    im2 = ax2.imshow(traffic_data, cmap='viridis', vmin=0, vmax=100)
    ax2.set_title("Загруженность %")

    # Заполненная область
    t = np.linspace(0, 10, 100)
    y = np.sin(t) * np.exp(-t / 10)
    ax3.fill_between(t, y, alpha=0.3, color='green');
    ax3.plot(t, y)
    ax3.set_title("Область под кривой")

    # Контурная карта
    X, Y = np.meshgrid(np.linspace(-3, 3, 30), np.linspace(-3, 3, 30))
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
    ax4.contourf(X, Y, Z, levels=20, cmap='plasma')
    ax4.set_title("Контурная карта")

    plt.colorbar(im1, ax=ax1);
    plt.colorbar(im2, ax=ax2)
    canvas.draw()


tk.Button(root, text="Обновить данные", command=update_maps).pack(pady=10)
tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, label="Интенсивность").pack()

update_maps()
root.mainloop()
