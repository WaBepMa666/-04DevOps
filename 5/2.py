import tkinter as tk
import math
from datetime import datetime


class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Красивые аналоговые часы")
        self.root.configure(bg="#0a0e17")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Canvas для циферблата
        self.canvas = tk.Canvas(root, width=350, height=350, bg="#0f1419",
                                highlightthickness=0)
        self.canvas.pack(pady=30)

        self.center_x = 175
        self.center_y = 175
        self.radius = 150

        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        # Фон циферблата
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius,
                                fill="#1a1f28", outline="#3a4350", width=8)

        # Главная окружность
        self.canvas.create_oval(self.center_x - self.radius + 8, self.center_y - self.radius + 8,
                                self.center_x + self.radius - 8, self.center_y + self.radius - 8,
                                outline="#4a5a70", width=6)

        # Цифры 1-12 (ровно по окружности)
        for hour in range(1, 13):
            angle = math.radians(90 - (hour * 30))  # 12=90°, 3=0°, 6=-90°, 9=-180°
            x = self.center_x + (self.radius - 35) * math.cos(angle)
            y = self.center_y - (self.radius - 35) * math.sin(angle)

            self.canvas.create_text(x, y, text=str(hour), fill="#e8f4f8",
                                    font=("Segoe UI", 16, "bold"))

        # Маленькие деления (каждые 6°)
        for i in range(60):
            angle = math.radians(90 - (i * 6))
            inner_x = self.center_x + (self.radius - 15) * math.cos(angle)
            inner_y = self.center_y - (self.radius - 15) * math.sin(angle)
            outer_x = self.center_x + (self.radius - 5) * math.cos(angle)
            outer_y = self.center_y - (self.radius - 5) * math.sin(angle)

            self.canvas.create_line(inner_x, inner_y, outer_x, outer_y,
                                    fill="#90a4ae", width=2)

    def update_clock(self):
        self.canvas.delete("hand")  # Удаляем старые стрелки

        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second

        # Углы стрелок (в радианах)
        hour_angle = math.radians(90 - ((h % 12) * 30 + m * 0.5))
        minute_angle = math.radians(90 - (m * 6))
        second_angle = math.radians(90 - (s * 6))

        # Часовая стрелка
        hour_x = self.center_x + (self.radius - 50) * math.cos(hour_angle)
        hour_y = self.center_y - (self.radius - 50) * math.sin(hour_angle)
        self.canvas.create_line(self.center_x, self.center_y, hour_x, hour_y,
                                fill="#4fc3f7", width=8, capstyle="round", tags="hand")

        # Минутная стрелка
        minute_x = self.center_x + (self.radius - 30) * math.cos(minute_angle)
        minute_y = self.center_y - (self.radius - 30) * math.sin(minute_angle)
        self.canvas.create_line(self.center_x, self.center_y, minute_x, minute_y,
                                fill="#e0e0e0", width=5, capstyle="round", tags="hand")

        # Секундная стрелка
        second_x = self.center_x + (self.radius - 20) * math.cos(second_angle)
        second_y = self.center_y - (self.radius - 20) * math.sin(second_angle)
        self.canvas.create_line(self.center_x, self.center_y, second_x, second_y,
                                fill="#ff5252", width=3, capstyle="round", tags="hand")

        # Центральный кружок
        self.canvas.create_oval(self.center_x - 10, self.center_y - 10,
                                self.center_x + 10, self.center_y + 10,
                                fill="#ffffff", outline="#ff5252", width=2)

        # Цифровое время снизу
        time_str = now.strftime("%H:%M:%S")
        self.canvas.create_text(self.center_x, self.center_y + 40, text=time_str,
                                fill="#ffffff", font=("Segoe UI", 20, "bold"))

        # Обновление через 200мс (плавная секундная стрелка)
        self.root.after(200, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
