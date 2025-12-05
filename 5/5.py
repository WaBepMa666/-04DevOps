import tkinter as tk
import math

MIN_SPEED = 0
MAX_SPEED = 180
MIN_ANGLE = 120  # 0 км/ч справа
MAX_ANGLE = -120  # max слева

CANVAS_W = 600
CANVAS_H = 400  # Увеличил высоту для лучшего отображения


class Speedometer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Спидометр")
        self.config(bg="#0a0e14")

        # Устанавливаем размер окна
        self.geometry("700x550")
        self.minsize(700, 550)

        # Главный контейнер
        main_container = tk.Frame(self, bg="#0a0e14")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # ----- СПИДОМЕТР -----
        meter_frame = tk.Frame(main_container, bg="#0a0e14")
        meter_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(
            meter_frame,
            width=CANVAS_W,
            height=CANVAS_H,
            bg="#151821",
            highlightthickness=2,
            highlightbackground="#1e2129",
        )
        self.canvas.pack(expand=True)

        # ----- ПАНЕЛЬ УПРАВЛЕНИЯ -----
        control_frame = tk.Frame(main_container, bg="#0a0e14")
        control_frame.pack(fill="x", pady=(20, 0))

        # Текст "Скорость"
        tk.Label(
            control_frame,
            text="Скорость:",
            bg="#0a0e14",
            fg="#e0f2f1",
            font=("Segoe UI", 12, "bold"),
        ).pack(side="left", padx=(0, 10))

        # Слайдер
        slider_container = tk.Frame(control_frame, bg="#0a0e14")
        slider_container.pack(side="left", fill="x", expand=True, padx=10)

        self.slider = tk.Scale(
            slider_container,
            from_=MIN_SPEED,
            to=MAX_SPEED,
            orient="horizontal",
            showvalue=0,
            length=400,
            bg="#0a0e14",
            troughcolor="#263238",
            activebackground="#37474f",
            fg="#cfd8dc",
            highlightthickness=0,
            sliderrelief="flat",
            sliderlength=20,
            command=self.on_change,
        )
        self.slider.set(0)
        self.slider.pack(fill="x", expand=True)

        # Отображение значения скорости
        self.value_label = tk.Label(
            control_frame,
            text="0 км/ч",
            bg="#0a0e14",
            fg="#ffffff",
            font=("Segoe UI", 16, "bold"),
            width=8,
        )
        self.value_label.pack(side="right", padx=(10, 0))

        # Параметры спидометра
        self.cx = CANVAS_W // 2
        self.cy = int(CANVAS_H * 0.65)  # Центр смещён выше для красивого отображения
        self.r_outer = int(CANVAS_H * 0.5)
        self.r_inner = int(self.r_outer * 0.5)

        self.current_speed = 0
        self.needle_id = None
        self.text_id = None

        self.draw_face()

    def polar(self, r, angle_deg):
        """Конвертирует полярные координаты в декартовы"""
        a = math.radians(angle_deg)
        return self.cx + r * math.cos(a), self.cy - r * math.sin(a)

    def draw_face(self):
        """Рисует основу спидометра"""
        c = self.canvas
        c.delete("all")

        # Фон спидометра
        c.create_rectangle(
            0, 0,
            CANVAS_W, CANVAS_H,
            fill="#151821",
            outline="",
        )

        # Внешний круг спидометра с градиентным эффектом
        for i in range(5):
            offset = i * 2
            c.create_oval(
                self.cx - self.r_outer - offset,
                self.cy - self.r_outer - offset,
                self.cx + self.r_outer + offset,
                self.cy + self.r_outer + offset,
                outline="#1e2129",
                width=1,
            )

        # Основная дуга шкалы
        c.create_arc(
            self.cx - self.r_outer,
            self.cy - self.r_outer,
            self.cx + self.r_outer,
            self.cy + self.r_outer,
            start=MIN_ANGLE,
            extent=MAX_ANGLE - MIN_ANGLE,
            style="arc",
            outline="#4fc3f7",
            width=6,
        )

        # Деления и цифры
        for v in range(MIN_SPEED, MAX_SPEED + 1, 10):
            k = (v - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)
            ang = MIN_ANGLE + (MAX_ANGLE - MIN_ANGLE) * k
            is_main = (v % 20 == 0)

            # Основные и второстепенные деления
            if is_main:
                r1 = self.r_outer - 15
                r2 = self.r_outer - 35
                color = "#ffffff"
                width = 3
            else:
                r1 = self.r_outer - 15
                r2 = self.r_outer - 25
                color = "#90a4ae"
                width = 1

            x1, y1 = self.polar(r1, ang)
            x2, y2 = self.polar(r2, ang)
            c.create_line(
                x1, y1, x2, y2,
                fill=color,
                width=width,
            )

            # Цифры для основных делений
            if is_main and v <= 160:  # Ограничиваем цифры до 160
                tx, ty = self.polar(self.r_outer - 55, ang)
                c.create_text(
                    tx, ty,
                    text=str(v),
                    fill="#eceff1",
                    font=("Segoe UI", 11, "bold"),
                )

        # Внутренняя маска
        c.create_oval(
            self.cx - self.r_inner,
            self.cy - self.r_inner,
            self.cx + self.r_inner,
            self.cy + self.r_inner,
            fill="#1a1d26",
            outline="#263238",
            width=3,
        )

        # Центральная точка
        c.create_oval(
            self.cx - 12,
            self.cy - 12,
            self.cx + 12,
            self.cy + 12,
            fill="#ffffff",
            outline="#ff5252",
            width=3,
        )

        # Подпись единицы измерения
        c.create_text(
            self.cx,
            self.cy + 35,
            text="km/h",
            fill="#90caf9",
            font=("Segoe UI", 14, "bold"),
        )

        # Отображение текущей скорости
        self.draw_needle(self.current_speed)

    def draw_needle(self, speed):
        """Рисует стрелку и цифровое отображение скорости"""
        c = self.canvas

        # Удаляем предыдущую стрелку и текст
        if self.needle_id is not None:
            c.delete(self.needle_id)
        if self.text_id is not None:
            c.delete(self.text_id)

        # Вычисляем угол стрелки
        k = (speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)
        k = max(0.0, min(1.0, k))
        ang = MIN_ANGLE + (MAX_ANGLE - MIN_ANGLE) * k

        # Координаты для треугольной стрелки
        x_end, y_end = self.polar(self.r_outer - 40, ang)  # Кончик стрелки
        x_left, y_left = self.polar(18, ang + 90)  # Левая точка основания
        x_right, y_right = self.polar(18, ang - 90)  # Правая точка основания

        # Рисуем стрелку с градиентным эффектом
        self.needle_id = c.create_polygon(
            x_left, y_left,
            x_end, y_end,
            x_right, y_right,
            fill="#ff5252",
            outline="#ff8a80",
            width=1,
            smooth=True,
        )

        # Цифровое отображение скорости в центре
        self.text_id = c.create_text(
            self.cx,
            self.cy - 5,
            text=str(int(speed)),
            fill="#ffffff",
            font=("Segoe UI", 36, "bold"),
        )

        # Добавляем тень для текста
        c.create_text(
            self.cx + 1,
            self.cy - 4,
            text=str(int(speed)),
            fill="#4a4a4a",
            font=("Segoe UI", 36, "bold"),
        )

    def on_change(self, val):
        """Обработчик изменения слайдера"""
        self.current_speed = float(val)
        self.value_label.config(text=f"{int(self.current_speed)} км/ч")

        # Плавное обновление стрелки (перерисовываем только стрелку, а не весь спидометр)
        self.draw_needle(self.current_speed)


if __name__ == "__main__":
    app = Speedometer()
    app.mainloop()