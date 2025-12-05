# 5. Интерактивная сказка
import tkinter as tk
pygame.mixer.init()

pages = [
    ("🐺 Волк и семеро козлят\nКоза ушла за едой...", 'page1.wav'),
    ("Козлята! Не открывайте никому!\nПостучали в дверь...", 'page2.wav')
]
current_page = 0

root = tk.Tk()
root.title("📖 Сказка")
root.geometry("350x300")
root.configure(bg='lightblue')

text_label = tk.Label(root, text=pages[0][0], font=('Arial', 14), wraplength=300,
                      justify='center', bg='lightblue')
text_label.pack(pady=20)

def play_page():
    pygame.mixer.Sound(pages[current_page][1]).play()

def next_page():
    global current_page
    current_page = (current_page + 1) % len(pages)
    text_label.config(text=pages[current_page][0])

tk.Button(root, text="🔊 Слушать", width=12, height=2, command=play_page).pack(pady=10)
tk.Button(root, text="➡️ Следующая", width=12, height=2, command=next_page).pack(pady=10)

objects_frame = tk.Frame(root, bg='lightblue')
objects_frame.pack(pady=10)
tk.Button(objects_frame, text="🐑", width=4, command=lambda: pygame.mixer.Sound('sheep.wav').play()).pack(side='left')
tk.Button(objects_frame, text="🐺", width=4, command=lambda: pygame.mixer.Sound('wolf.wav').play()).pack(side='left')
root.mainloop()
