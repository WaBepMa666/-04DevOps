# 4. Виртуальный оркестр (Launchpad)
import tkinter as tk
pygame.mixer.init()

instruments = {
    '🥁': 'drum.wav', '🎹': 'piano.wav', '🎻': 'violin.wav', '🎺': 'trumpet.wav'
}
active = set()

root = tk.Tk()
root.title("🎼 Детский оркестр")
root.geometry("350x200")
root.configure(bg='black')

def toggle_instrument(icon):
    if icon in active:
        active.remove(icon)
        btn = root.children[f'!button{icon}']
        btn.configure(relief='raised')
    else:
        active.add(icon)
        btn = root.children[f'!button{icon}']
        btn.configure(relief='sunken')
    play_orchestra()

def play_orchestra():
    for instr in active:
        pygame.mixer.Sound(instruments[instr]).play()

for i, icon in enumerate(instruments):
    btn = tk.Button(root, text=icon, bg='gold', fg='black', font=('Arial', 24),
                    width=4, height=2, command=lambda i=icon: toggle_instrument(i))
    btn.grid(row=i//2, column=i%2, padx=10, pady=10)

tk.Button(root, text="🎵 ИГРАТЬ ВСЕ", bg='red', fg='white', width=15,
          command=play_orchestra).grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
