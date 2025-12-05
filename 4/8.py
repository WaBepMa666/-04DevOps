# 8. Угадай инструмент
import tkinter as tk
import random

pygame.mixer.init()

instruments = {
    '🥁': 'drum.wav', '🎹': 'piano.wav',
    '🎸': 'guitar.wav', '🎷': 'sax.wav'
}
current = random.choice(list(instruments.keys()))

root = tk.Tk()
root.title("🎼 Угадай инструмент!")
root.geometry("300x300")

score = 0


def play_instrument():
    pygame.mixer.Sound(instruments[current]).play()


def check_answer(choice):
    global score, current
    if choice == current:
        score += 1
        result.config(text=f"✅ +1! Очки: {score}", fg='green')
    else:
        result.config(text="❌ Нет, попробуй еще", fg='red')

    root.after(1500, new_instrument)


def new_instrument():
    global current
    current = random.choice(list(instruments.keys()))
    result.config(text="Слушай внимательно!")
    play_btn.config(command=play_instrument)


tk.Label(root, text="Какой инструмент?", font=('Arial', 16)).pack(pady=20)
play_btn = tk.Button(root, text="🔊 Слушать", width=12)
play_btn.pack(pady=10)

for icon in instruments:
    tk.Button(root, text=icon, width=8, height=2,
              command=lambda i=icon: check_answer(i)).pack(pady=5)

result = tk.Label(root, text="Очки: 0", font=('Arial', 14))
result.pack(pady=10)
root.mainloop()
