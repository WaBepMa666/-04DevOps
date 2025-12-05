# 6. Игра "Повтори мелодию"
import tkinter as tk
import random
pygame.mixer.init()

notes = ['C.wav', 'D.wav', 'E.wav', 'F.wav', 'G.wav']
melody = random.choices(notes, k=3)
current_note = 0

root = tk.Tk()
root.title("🎵 Повтори мелодию")
root.geometry("300x350")

def play_melody():
    global current_note
    current_note = 0
    play_next_note()

def play_next_note():
    global current_note
    if current_note < len(melody):
        pygame.mixer.Sound(melody[current_note]).play()
        current_note += 1
        root.after(800, play_next_note)

def check_note(note):
    global current_note
    if note == melody[current_note]:
        current_note += 1
        result.config(text=f"✓ {current_note}/{len(melody)}", fg='green')
        if current_note == len(melody):
            result.config(text="🎉 Отлично!", fg='gold')
    else:
        result.config(text="❌ Попробуй еще", fg='red')

tk.Label(root, text="Слушай и повторяй!", font=('Arial', 14)).pack(pady=10)
tk.Button(root, text="🔊 Проиграть", command=play_melody).pack(pady=10)

for i, note in enumerate(['До', 'Ре', 'Ми', 'Фа', 'Соль']):
    tk.Button(root, text=note, width=8, command=lambda n=notes[i]: check_note(n)).pack(pady=3)

result = tk.Label(root, text="Нажми 'Проиграть'", font=('Arial', 12))
result.pack(pady=20)
root.mainloop()
