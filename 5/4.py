import tkinter as tk
import math

BG_WIN = "#05070b"
BG_PANEL = "#151821"
ANG_MIN = -120
ANG_MAX = 120

class GoodBadGauge(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GOOD / BAD шкала")
        self.configure(bg=BG_WIN)

        # разрешаем менять размер
        self.minsize(640, 360)

        # флаг фуллскрина + кнопка
        self.is_fullscreen = False

        top_bar = tk.Frame(self, bg=BG_WIN)
        top_bar.pack(fill="x", padx=10, pady=(5, 0))
        self.fs_btn = tk.Button(
            top_bar, text="Во весь экран",
            command=self.toggle_fullscreen,
            bg="#263238", fg="#ffffff", relief="flat"
        )
        self.fs_btn.pack(side="right")

        # канва занимает всё доступное место сверху
        self.canvas = tk.Canvas(self, bg=BG_PANEL, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=15, pady=(5, 0))

        # блок с ползунком снизу
        controls = tk.Frame(self, bg=BG_WIN)
        controls.pack(fill="x", padx=15, pady=10)

        tk.Label(controls, text="Значение:",
                 fg="#e0f2f1", bg=BG_WIN,
                 font=("Segoe UI", 11)).pack(side="left")

        self.value_label = tk.Label(
            controls, text="40 %",
            fg="#ffffff", bg=BG_WIN,
            font=("Segoe UI", 14, "bold")
        )
        self.value_label.pack(side="right")

        self.scale = tk.Scale(
            controls, from_=0, to=100,
            orient="horizontal", showvalue=0,
            bg=BG_WIN, troughcolor="#263238",
            highlightthickness=0, fg="#cfd8dc"
        )
        self.scale.set(40)
        self.scale.pack(side="right", padx=(10, 0), fill="x", expand=True)
        self.scale.configure(command=self.on_change)

        # при ресайзе окна – перерисовываем шкалу
        self.canvas.bind("<Configure>", self.on_resize)

        self.current_value = 40
        self.redraw()

    # ---------- полноэкранный режим ----------
    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        self.attributes("-fullscreen", self.is_fullscreen)
        self.fs_btn.config(text="Обычный режим" if self.is_fullscreen else "Во весь экран")

    # ---------- геометрия ----------
    def polar_to_xy(self, cx, cy, r, angle_deg):
        a = math.radians(angle_deg)
        return cx + r * math.cos(a), cy - r * math.sin(a)

    # ---------- отрисовка ----------
    def redraw(self):
        c = self.canvas
        c.delete("all")

        w = c.winfo_width()
        h = c.winfo_height()

        # центр и радиусы зависят от текущего размера канвы
        cx = w // 2
        cy = int(h * 0.65)          # чуть выше низа
        r_out = int(min(w, h) * 0.35)
        r_in = int(r_out * 0.6)

        # рамка панели
        margin_x = int(w * 0.08)
        c.create_rectangle(
            margin_x, int(h * 0.15),
            w - margin_x, h - int(h * 0.2),
            fill=BG_PANEL, outline="#101318", width=3
        )

        # цветные сектора
        segments = [
            (ANG_MIN,      48, "#4caf50"),
            (ANG_MIN+48,   48, "#8bc34a"),
            (ANG_MIN+96,   48, "#cddc39"),
            (ANG_MIN+144,  48, "#ffeb3b"),
            (ANG_MIN+192,  48, "#ff9800"),
            (ANG_MIN+240,  48, "#f44336"),
        ]
        for start, ext, col in segments:
            x0, y0 = cx - r_out, cy - r_out
            x1, y1 = cx + r_out, cy + r_out
            c.create_arc(
                x0, y0, x1, y1,
                start=start, extent=ext,
                outline="", fill=col, style="pieslice"
            )

        # вырезаем центр
        c.create_oval(cx - r_in, cy - r_in, cx + r_in, cy + r_in,
                      outline="", fill=BG_PANEL)

        # дуга контура
        c.create_arc(
            cx - r_out, cy - r_out, cx + r_out, cy + r_out,
            start=ANG_MIN, extent=ANG_MAX - ANG_MIN,
            style="arc", outline="#eceff1", width=3
        )

        # GOOD / BAD – чуть ниже дуги, так что их не обрежет
        gx, gy = self.polar_to_xy(cx, cy, r_out + 15, ANG_MIN + 30)
        bx, by = self.polar_to_xy(cx, cy, r_out + 15, ANG_MAX - 30)
        c.create_text(gx, gy, text="GOOD",
                      fill="#e8f5e9", font=("Segoe UI", 14, "bold"))
        c.create_text(bx, by, text="BAD",
                      fill="#ffebee", font=("Segoe UI", 14, "bold"))

        # знак процента
        c.create_text(cx, cy, text="%",
                      fill="#ffffff", font=("Segoe UI", 24, "bold"))

        # рисуем стрелку и число
        self.draw_needle(cx, cy, r_out, self.current_value)

    def draw_needle(self, cx, cy, r_out, value):
        c = self.canvas
        c.delete("needle")

        k = value / 100.0
        angle = ANG_MIN + (ANG_MAX - ANG_MIN) * k
        x_end, y_end = self.polar_to_xy(cx, cy, r_out - 15, angle)

        c.create_line(cx, cy, x_end, y_end,
                      fill="#ffffff", width=4,
                      capstyle="round", tags="needle")
        c.create_oval(cx-8, cy-8, cx+8, cy+8,
                      fill="#ffffff", outline="#263238",
                      width=2, tags="needle")

        # подпись значения чуть ниже центра, всегда внутри панели
        c.create_text(cx, cy + 50,
                      text=f"{value} %",
                      fill="#ffffff",
                      font=("Segoe UI", 18, "bold"),
                      tags="needle")

    # ---------- события ----------
    def on_change(self, val):
        self.current_value = int(float(val))
        self.value_label.config(text=f"{self.current_value} %")
        self.redraw()

    def on_resize(self, event):
        # при любом изменении размеров – полностью пересчитываем шкалу
        self.redraw()

if __name__ == "__main__":
    GoodBadGauge().mainloop()
