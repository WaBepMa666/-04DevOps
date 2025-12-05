# 2. Интерактивная раскраска с музыкой
import tkinter as tk
pygame.mixer.init()

colors = ['red', 'blue', 'green', 'yellow', 'purple']
sounds = {c: pygame.mixer.Sound(f'{c}.wav') for c in colors}

root = tk.Tk()
root.title("🎨 Раскраска с музыкой")
root.geometry("350x400")
canvas = tk.Canvas(root, width=200, height=200, bg='white')
canvas.pack(pady=20)
canvas.create_oval(50,50,150,150, fill='white', outline='black', width=3)

def paint_color(color):
    sounds[color].play()
    x,y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_oval(x-5,y-5,x+5,y+5, fill=color, outline=color)

paint_btns = []
for i, color in enumerate(colors):
    btn = tk.Button(root, text=color.upper(), bg=color, fg='white', width=8,
                    command=lambda c=color: paint_color(c))
    btn.pack(pady=5)
    paint_btns.append(btn)

canvas.bind('<B1-Motion>', lambda e: paint_color('black'))
tk.Label(root, text="Выбери цвет и рисуй! 🎵", font=('Arial', 14)).pack()
root.mainloop()
