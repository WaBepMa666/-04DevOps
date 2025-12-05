import tkinter as tk
import math

BG_PANEL = "#232a36"
BG_WIN = "#191929"
BG_BTN = "#252c39"
HILIGHT = "#96eaff"
FG_ON = "#00ffc2"
FG_OFF = "#ff4444"
TXT_FG = "#eef9ff"

class FancyButton:
    """Ровная кнопка на Canvas с независимой подписью."""
    def __init__(self, canvas, figures, command):
        self.canvas = canvas
        self.figures = figures
        self.command = command
        # события только на кнопки, не на надпись
        for fig in figures:
            canvas.tag_bind(fig, "<Enter>", self.on_enter)
            canvas.tag_bind(fig, "<Leave>", self.on_leave)
            canvas.tag_bind(fig, "<ButtonPress-1>", self.on_down)
            canvas.tag_bind(fig, "<ButtonRelease-1>", self.on_up)
        self.normal_outline = canvas.itemcget(figures[0], "outline")

    def on_enter(self, _):
        for fig in self.figures:
            self.canvas.itemconfigure(fig, outline=HILIGHT, width=4)
    def on_leave(self, _):
        for fig in self.figures:
            self.canvas.itemconfigure(fig, outline=self.normal_outline, width=3)
    def on_down(self, _):
        for fig in self.figures:
            self.canvas.move(fig, 0, 2)
    def on_up(self, _):
        for fig in self.figures:
            self.canvas.move(fig, 0, -2)
        if self.command:
            self.command()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Очень красивые ровные кнопки")
        self.configure(bg=BG_WIN)
        self.geometry("950x460")

        self.canvas = tk.Canvas(self, width=900, height=390, bg=BG_PANEL, highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        # Кнопки и их подписи
        self.add_buttons()

        self.status = tk.Label(self, text="Готово", font=("Segoe UI",14),
                               bg=BG_WIN, fg="#aaeaff")
        self.status.pack(fill="x", pady=(0,10))

    def add_buttons(self):
        c = self.canvas

        # 1. Классическая круглая PLAY кнопка
        cx, cy = 120, 160
        oval1 = c.create_oval(cx-50, cy-50, cx+50, cy+50, fill=BG_BTN, outline="#bfefff", width=3)
        oval2 = c.create_oval(cx-33, cy-33, cx+33, cy+33, fill="#111820", outline="#02fafe", width=2)
        # “Play”
        play = c.create_polygon([
            cx-10, cy-18,
            cx-10, cy+18,
            cx+23, cy
        ], fill="#ffffff", outline="#bfefff", width=2)
        FancyButton(c, [oval1, oval2, play], lambda: self.set_status("PLAY"))
        c.create_text(cx, cy+70, text="PLAY", fill=TXT_FG, anchor="center", font=("Segoe UI", 13, "bold"))

        # 2. Треугольная кнопка
        cx, cy = 300, 160
        pts = []
        for i in range(3):
            angle = math.radians(90 + 120 * i)
            pts += [cx + 48 * math.cos(angle), cy + 48 * math.sin(angle)]
        tri = c.create_polygon(pts, fill="#e57373", outline="#ffbcaf", width=3)
        FancyButton(c, [tri], lambda: self.set_status("TRIANGLE"))
        c.create_text(cx, cy+70, text="TRIANGLE", fill=TXT_FG, anchor="center", font=("Segoe UI", 13, "bold"))

        # 3. Шестиугольная кнопка
        cx, cy = 480, 160
        pts = []
        for i in range(6):
            angle = math.radians(30 + 60 * i)
            pts += [cx + 43 * math.cos(angle), cy + 43 * math.sin(angle)]
        hexagon = c.create_polygon(pts, fill="#455c55", outline="#c7ffe5", width=3)
        FancyButton(c, [hexagon], lambda: self.set_status("HEX"))
        c.create_text(cx, cy+70, text="HEX", fill=TXT_FG, anchor="center", font=("Segoe UI", 13, "bold"))

        # 4. Овальная двойная
        cx, cy = 660, 160
        oval_outer = c.create_oval(cx-80, cy-35, cx+80, cy+35, fill="#292e33", outline="#aaeaff", width=3)
        oval_inner = c.create_oval(cx-65, cy-22, cx+65, cy+22, fill="#304050", outline="#99edec", width=2)
        pause = c.create_text(cx, cy, text="▶║", fill="#ffffff", font=("Segoe UI",22,"bold"))
        FancyButton(c, [oval_outer, oval_inner, pause], lambda: self.set_status("PAUSE"))
        c.create_text(cx, cy+60, text="PAUSE", fill=TXT_FG, anchor="center", font=("Segoe UI", 13, "bold"))

        # 5. Круглая POWER кнопка
        cx, cy = 255, 320
        ov = c.create_oval(cx-47, cy-47, cx+47, cy+47, fill=BG_BTN, outline="#6ffdcb", width=3)
        ring = c.create_oval(cx-24, cy-24, cx+24, cy+24, outline=FG_ON, width=4)
        stem = c.create_line(cx,cy-30,cx,cy+8,fill=FG_ON,width=5,capstyle="round")
        FancyButton(c, [ov, ring, stem], lambda: self.set_status("POWER"))
        c.create_text(cx, cy+60, text="POWER", fill=TXT_FG, anchor="center", font=("Segoe UI", 13, "bold"))

        # 6. Прямоугольная ON/OFF
        cx, cy = 535, 320
        frame = c.create_rectangle(cx-66,cy-38,cx+66,cy+38,fill="#202226",outline="#d4ecff",width=3)
        up = c.create_rectangle(cx-60,cy-32,cx+60,cy,fill="#18c065",outline="#b9f5e0",width=2)
        dn = c.create_rectangle(cx-60,cy,cx+60,cy+32,fill="#e5004d",outline="#fee3e1",width=2)
        FancyButton(c, [frame, up, dn], lambda: self.set_status("ON/OFF"))
        c.create_text(cx, cy+54, text="ON / OFF", fill=TXT_FG, anchor="center", font=("Segoe UI", 13, "bold"))

    def set_status(self, s):
        self.status.config(text=f"НАЖАТА: {s}")

if __name__ == "__main__":
    App().mainloop()
