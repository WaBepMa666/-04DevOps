# 5. Графики и диаграммы (Chart1)
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.title("Chart1 - Диаграммы")
root.geometry("800x600")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12,8))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

data_types = ['Столбцы', 'Круг', 'Линия', 'Тепловая карта']
current_data = np.random.rand(5, 5)

def update_charts():
    ax1.clear(); ax1.bar(['A','B','C','D'], np.random.rand(4)); ax1.set_title("Столбцы")
    ax2.clear(); ax2.pie(np.random.rand(4), labels=['A','B','C','D']); ax2.set_title("Круговая")
    ax3.clear(); t = np.linspace(0,10,100); ax3.plot(t, np.sin(t)); ax3.set_title("Синус")
    ax4.clear(); ax4.imshow(current_data, cmap='hot'); ax4.set_title("Тепловая карта")
    canvas.draw()

tk.Button(root, text="Обновить данные", command=update_charts).pack(pady=10)
tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, command=lambda x: setattr(current_data, 'data', np.random.rand(5,5))).pack()

update_charts()
root.mainloop()
