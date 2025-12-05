# 3. Игра "Найди звук"
import tkinter as tk
import random
pygame.mixer.init()

animals = {'🐶': 'dog.wav', '🐱': 'cat.wav', '🐭': 'mouse.wav'}
current_sound = random.choice(list(animals.keys()))

root = tk.Tk()
root.title("🎮 Найди звук!")
root.geometry("300x250")

def play_sound():
    pygame.mixer.Sound(animals[current_sound]).play()

def check_answer(choice):
    if choice == current_sound:
        result.config(text="✅ Правильно!", fg='green')
    else:
        result.config(text="❌ Попробуй еще!", fg='red')
    root.after(2000, new_game)

def new_game():
    global current_sound
    current_sound = random.choice(list(animals.keys()))
    result.config(text="Слушай внимательно!")
    play_btn.config(command=play_sound)

tk.Label(root, text="Что звучит?", font=('Arial', 16)).pack(pady=20)
play_btn = tk.Button(root, text="🔊 Слушать", width=12, height=2)
play_btn.pack(pady=10)

for animal in animals:
    tk.Button(root, text=animal, width=10, height=2,
              command=lambda a=animal: check_answer(a)).pack(pady=5)

result = tk.Label(root, text="Слушай внимательно!", font=('Arial', 12))
result.pack(pady=10)
root.mainloop()
