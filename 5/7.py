import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Диапазон действительной и мнимой части
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.linspace(-2*np.pi, 2*np.pi, 200)
X, Y = np.meshgrid(x, y)

# Комплексная переменная
Z_complex = np.sin(X + 1j*Y)

# Модуль функции для 3D отображения
Z = np.abs(Z_complex)

# Создание 3D графика
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Поверхность
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
ax.set_zlabel("|sin(z)|")
ax.set_title("3D отображение функции sin(z) в комплексной плоскости")

fig.colorbar(surf, shrink=0.5, aspect=10, label="Амплитуда")
plt.show()
