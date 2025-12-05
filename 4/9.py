# 9. Интерактивный метроном с визуализацией
import tkinter as tk
import pygame
import threading
import time

pygame.mixer.init()
tick_sound = pygame.mixer.Sound(buffer=bytes([65]*2000))  # Простой beep

root = tk.Tk()
root.title("🎵 Метроном для детей")
root.geometry("300x400")
root.configure(bg='black')

is_running = False
bpm = tk.IntVar(value=120)
beat = tk.IntVar(value=0)

def metronome_tick():
    global is_running, beat
    while is_running:
        tick_sound.play()
        beat.set((beat.get() + 1) % 4)
        circle.configure(bg='red' if beat.get() == 0 else 'yellow')
        time.sleep(60 / bpm.get())

def start_stop():
    global is_running
    is_running = not is_running
    if is_running:
        btn_start.config(text="⏹️ СТОП")
        threading.Thread(target=metronome_tick, daemon=True).start()
    else:
        btn_start.config(text="▶️ СТАРТ")
        beat.set(0)
        circle.configure(bg='gray')

# Большой мигающий круг
