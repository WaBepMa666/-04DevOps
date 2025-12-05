# 1. Интерактивный музыкальный инструмент для детей
import tkinter as tk
from tkinter import ttk
import pygame

pygame.mixer.init()
sounds = {
    'red': pygame.mixer.Sound('beep.wav'),  # Замените на реальные файлы
    'blue': pygame.mixer.Sound('kick.wav'),
    'green': pygame.mixer.Sound('bell.wav'),
    'yellow': pygame.mixer.Sound('snare.wav')
}

root = tk.Tk()
root.title("🎵 Музыка для детей")
root.geometry("400x300")
root.configure(bg='black')

def play_sound(color):
    sounds[color].play()
    btn = root.children[f'!button{color}']
    btn.configure(bg='white')
    root.after(200, lambda: btn.configure(bg=color))

colors = [('Красный', 'red'), ('Синий', 'blue'), ('Зеленый', 'green'), ('Желтый', 'yellow')]
for i, (name, color) in enumerate(colors):
    btn = tk.Button(root, text=name, bg=color, fg='white', font=('Arial', 16),
                    width=12, height=3, command=lambda c=color: play_sound(c))
    btn.grid(row=i//2, column=i%2, padx=10, pady=10)

tk.Label(root, text="Нажимай кнопки! 🎶", fg='white', bg='black', font=('Arial', 20)).grid(row=2, column=0, columnspan=2)
root.mainloop()
