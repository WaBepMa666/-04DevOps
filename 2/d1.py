import tkinter as tk
import math

WIDTH = 320
HEIGHT = 220
RADIUS = 90
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT - 35
MIN_SPEED = 0
MAX_SPEED = 180
MIN_ANGLE = -120
MAX_ANGLE = 120

def speed_to_angle(speed):
    # Преобразует скорость в угол поворота стрелки
    norm = (speed - MIN_SPEED)/(MAX_SPEED-MIN_SPEED)
    angle = MIN_ANGLE + (MAX_ANGLE - MIN_ANGLE)*norm
    return angle

def draw_speedometer(canvas):
    # Фон
    canvas.create_oval(CENTER_X-RADIUS-16, CENTER_Y-RADIUS-16,
                       CENTER_X+RADIUS+16, CENTER_Y+RADIUS+16,
                       fill="#101318", outline="#647485", width=5)
    # Полукруглая шкала
    canvas.create_arc(CENTER_X-RADIUS, CENTER_Y-RADIUS,
                      CENTER_X+RADIUS, CENTER_Y+RADIUS,
                      start=MIN_ANGLE, extent=MAX_ANGLE-MIN_ANGLE,
                      style="arc", outline="#50baff", width=7)
    # Риски и цифры
    for i in range(0, MAX_SPEED+1, 20):
        ang = math.radians(speed_to_angle(i))
        x1, y1 = CENTER_X + (RADIUS-5)*math.cos(ang), CENTER_Y - (RADIUS-5)*math.sin(ang)
        x2, y2 = CENTER_X + (RADIUS+18)*math.cos(ang), CENTER_Y - (RADIUS+18)*math.sin(ang)
        canvas.create_line(x1, y1, x2, y2, width=3, fill="#e5f4ff")
        # Метки
        tx, ty = CENTER_X + (RADIUS+35)*math.cos(ang), CENTER_Y - (RADIUS+28)*math.sin(ang)
        canvas.create_text(tx, ty, text=str(i), fill="#f6fcff", font=("Segoe UI", 13, "bold"))

    # Маленькие риски
    for i in range(MIN_SPEED, MAX_SPEED+1, 10):
        ang = math.radians(speed_to_angle(i))
        x1, y1 = CENTER_X + (RADIUS-8)*math.cos(ang), CENTER_Y - (RADIUS-8)*math.sin(ang)
        x2, y2 = CENTER_X + (RADIUS+9)*math.cos(ang), CENTER_Y - (RADIUS+9)*math.sin(ang)
        canvas.create_line(x1, y1, x2, y2, width=1, fill="#fff")

def set_speed(value):
    value = int(float(value))
    needle_angle = speed_to_angle(value)
    ang = math.radians(needle_angle)
    x = CENTER_X + (RADIUS-22)*math.cos(ang)
    y = CENTER_Y - (RADIUS-22)*math.sin(ang)
    canvas.coords("needle", CENTER_X, CENTER_Y, x, y)
    speed_label.config(text=f"{value} км/ч")

# GUI
root = tk.Tk()
root.title("Автомобильный спидометр")
root.configure(bg="#080d11")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#101318", highlightthickness=0)
canvas.pack(pady=(18, 0))

draw_speedometer(canvas)
# Стрелка, группа needle (чтобы coords легко обновлять)
canvas.create_line(CENTER_X, CENTER_Y,
                   CENTER_X, CENTER_Y-RADIUS+28,
                   width=6, fill="#ff5252", capstyle="round", tags="needle")
canvas.create_oval(CENTER_X-16, CENTER_Y-16, CENTER_X+16, CENTER_Y+16,
                   fill="#141821", outline="#fc5555", width=3)
canvas.create_oval(CENTER_X-6, CENTER_Y-6, CENTER_X+6, CENTER_Y+6,
                   fill="#ff5252", outline="white", width=1)

speed_label = tk.Label(root, text="0 км/ч", font=("Segoe UI", 20, "bold"), bg="#080d11", fg="#eaffff")
speed_label.pack(pady=(8,0))

speed_slider = tk.Scale(root, from_=MIN_SPEED, to=MAX_SPEED, orient="horizontal",
                        length=WIDTH-60, resolution=1, showvalue=0,
                        command=set_speed, bg="#11141b", troughcolor="#354866", fg="#c0def5",
                        sliderrelief="sunken")
speed_slider.pack(pady=5)
speed_slider.set(0)

root.mainloop()
