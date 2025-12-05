# 4. Аудио генератор + осциллограф
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sounddevice as sd
import soundfile as sf
import threading

root = tk.Tk()
root.title("Аудио генератор")
root.geometry("600x500")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

freq = tk.DoubleVar(value=440)
amp = tk.DoubleVar(value=0.5)
wave_type = tk.StringVar(value="sin")
duration = tk.DoubleVar(value=2.0)


def generate_wave():
    fs = 44100
    t = np.linspace(0, duration.get(), int(fs * duration.get()), False)

    if wave_type.get() == "sin":
        wave = amp.get() * np.sin(2 * np.pi * freq.get() * t)
    elif wave_type.get() == "square":
        wave = amp.get() * np.sign(np.sin(2 * np.pi * freq.get() * t))
    else:  # sawtooth
        wave = amp.get() * (2 * (t * freq.get() % 1) - 1)

    ax1.clear();
    ax1.plot(t[:1000], wave[:1000]);
    ax1.set_title("Осциллограмма")
    ax2.clear()
    Pxx, freqs = plt.psd(wave, Fs=fs, NFFT=2048)
    ax2.semilogy(freqs, Pxx);
    ax2.set_title("Спектр")
    canvas.draw()

    return wave, fs


def play_audio():
    wave, fs = generate_wave()
    sd.play(wave, fs)
    sd.wait()


def save_audio():
    wave, fs = generate_wave()
    filename = filedialog.asksaveasfilename(defaultextension=".wav")
    if filename:
        sf.write(filename, wave, fs)


tk.Scale(root, from_=100, to=2000, variable=freq, label="Частота").pack()
tk.Scale(root, from_=0.1, to=1, variable=amp, label="Амплитуда").pack()
tk.OptionMenu(root, wave_type, "sin", "square", "saw").pack()
tk.Scale(root, from_=0.5, to=5, variable=duration, label="Длительность").pack(pady=10)

tk.Button(root, text="Проиграть", command=play_audio).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Сохранить WAV", command=save_audio).pack(side=tk.LEFT, padx=10)
generate_wave()
root.mainloop()
