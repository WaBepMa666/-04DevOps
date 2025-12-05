# 7. Музыкальный конструктор (Drag & Drop упрощенный)
import tkinter as tk
pygame.mixer.init()

blocks = ['kick.wav', 'snare.wav', 'hihat.wav', 'bass.wav']
timeline = []

root = tk.Tk()
root.title("🎛️ Музыкальный конструктор")
root.geometry("400x300")

def add_block(sound):
    timeline.append(sound)
    update_timeline()
    pygame.mixer.Sound(sound).play()

def play_timeline():
    for sound in timeline:
        pygame.mixer.Sound(sound).play()
        root.after(300, lambda: None)

# Блоки для выбора
for i, sound in enumerate(['🥁', '💥', '✨', '🎸']):
    tk.Button(root, text=sound, bg='lightblue', width=6, height=2,
              command=lambda s=blocks[i]: add_block(s)).grid(row=0, column=i, padx=5)

# Таймлайн
timeline_frame = tk.Frame(root, bg='gray', height=100)
timeline_frame.pack(fill='x', pady=20)
timeline_frame.pack_propagate(False)

def update_timeline():
    for widget in timeline_frame.winfo_children():
        widget.destroy()
    for i, sound in enumerate(timeline):
        btn = tk.Button(timeline_frame, text='🟦', width=3,
                        command=lambda s=sound: pygame.mixer.Sound(s).play())
        btn.pack(side='left')

tk.Button(root, text="▶️ ИГРАТЬ", bg='green', fg='white', width=15,
          command=play_timeline).pack(pady=10)
root.mainloop()
