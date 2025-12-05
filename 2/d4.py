import tkinter as tk

WIDTH  = 140
HEIGHT = 46
RADIUS = HEIGHT // 2
ANIM_STEPS = 10
ANIM_DELAY = 15

class ToggleSwitch(tk.Canvas):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, width=WIDTH, height=HEIGHT,
                         bg=master["bg"], highlightthickness=0, **kwargs)
        self.command = command
        self.on = False
        self.animating = False

        self.track = self.create_rounded_rect(2, 2, WIDTH-2, HEIGHT-2,
                                              RADIUS, fill="#3b3f4a",
                                              outline="#111218", width=2)
        self.text_off = self.create_text(WIDTH*0.28, HEIGHT/2,
                                         text="OFF", fill="#ff7777",
                                         font=("Segoe UI", 11, "bold"))
        self.text_on = self.create_text(WIDTH*0.72, HEIGHT/2,
                                        text="ON",  fill="#9cffc8",
                                        font=("Segoe UI", 11, "bold"))

        self.knob_x_off = 2 + RADIUS
        self.knob_x_on  = WIDTH - 2 - RADIUS
        self.knob = self.create_oval(self.knob_x_off-RADIUS, 2,
                                     self.knob_x_off+RADIUS, HEIGHT-2,
                                     fill="#f4f5f7", outline="#c0c4cf", width=2)
        self.shadow = self.create_oval(self.knob_x_off-RADIUS, HEIGHT-6,
                                       self.knob_x_off+RADIUS, HEIGHT-1,
                                       fill="#151821", outline="")

        self.bind("<Button-1>", self.toggle)
        self.bind("<Enter>",  lambda e: self.itemconfigure(self.track, width=3))
        self.bind("<Leave>",  lambda e: self.itemconfigure(self.track, width=2))

    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r,
            x2, y2, x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def toggle(self, event=None):
        if self.animating:
            return
        self.on = not self.on
        self.animating = True
        self.animate_knob(0)

        if self.command:
            self.command(self.on)

    def animate_knob(self, step):
        if step > ANIM_STEPS:
            self.animating = False
            return
        t = step / ANIM_STEPS
        if self.on:
            x = self.knob_x_off + (self.knob_x_on - self.knob_x_off) * t
            track_color = self._blend("#3b3f4a", "#2ecc71", t)
        else:
            x = self.knob_x_on - (self.knob_x_on - self.knob_x_off) * t
            track_color = self._blend("#2ecc71", "#3b3f4a", t)
        self.itemconfigure(self.track, fill=track_color)
        dx = x - self.coords(self.knob)[0] - RADIUS
        self.move(self.knob, dx, 0)
        self.move(self.shadow, dx, 0)
        self.after(ANIM_DELAY, lambda: self.animate_knob(step + 1))

    @staticmethod
    def _blend(c1, c2, t):
        def to_rgb(c):
            return int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)
        r1, g1, b1 = to_rgb(c1)
        r2, g2, b2 = to_rgb(c2)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    BG_WIN = "#191b24"
    root = tk.Tk()
    root.title("Toggle Switch Demo")
    root.configure(bg=BG_WIN)
    root.geometry("300x150")

    def on_switch(state):
        print("ON" if state else "OFF")

    lbl = tk.Label(root, text="переключатель",
                   bg=BG_WIN, fg="#e0e4ff",
                   font=("Segoe UI", 12, "bold"))
    lbl.pack(pady=(20, 10))

    sw = ToggleSwitch(root, command=on_switch)
    sw.pack(pady=5)

    root.mainloop()
