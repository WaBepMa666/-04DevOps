# 10. Музыкальный пазл
import tkinter as tk
import random
pygame.mixer.init()
success_sound = pygame.mixer.Sound(buffer=bytes([70]*3000))  # Звук успеха

root = tk.Tk()
root.title("🧩 Музыкальный пазл")
root.geometry("400x350")
root.configure(bg='lightblue')

pieces = [0, 1, 2, 3]
random.shuffle(pieces)
puzzle_complete = False

canvas = tk.Canvas(root, width=300, height=200, bg='white', relief='raised')
canvas.pack(pady=20)

def draw_puzzle():
    canvas.delete("all")
    # Рамка пазла
    canvas.create_rectangle(20,20,280,180, fill='lightyellow', outline='black', width=3)
    # Части пазла (4 кусочка)
    for i in range(4):
        x, y = 50 + (i%2)*150, 50 + (i//2)*80
        color = 'green' if pieces[i] == i else 'gray'
        canvas.create_rectangle(x,y,x+90,y+60, fill=color, outline='black', width=2)
        canvas.create_text(x+45,y+30, text=str(i+1), font=('Arial', 16, 'bold'))

def check_puzzle():
    global puzzle_complete
    if pieces == [0,1,2,3]:
        puzzle_complete = True
        success_sound.play()
        result.config(text="🎉 Пазл собран! 🎵", fg='gold')
    else:
        result.config(text="🔄 Поставь цифры по порядку 1-2-3-4", fg='blue')

def move_piece(event):
    global pieces
    if puzzle_complete: return
    col = (event.x - 50) // 150
    row = (event.y - 50) // 80
    idx = row * 2 + col
    if 0 <= idx < 4:
        pieces[idx] = (pieces[idx] + 1) % 4
