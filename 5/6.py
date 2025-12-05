import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# ================================
#        Audio Meter Class
# ================================
class AudioMeter:
    def __init__(self, ax, title=""):
        self.ax = ax
        self.title = title
        self.level = 0
        self.max_level = 100
        self.bar_count = 60
        self.colors = []
        self.bars = []
        self._setup_plot()

    # -------------------------
    # Create gradient colors
    # -------------------------
    def _make_gradient(self):
        for i in range(self.bar_count):
            t = i / self.bar_count
            r = 0.2 + 0.5 * t
            g = 0.7 - 0.4 * t
            b = 1.0
            self.colors.append((r, g, b))

    # -------------------------
    # Initialize bar objects
    # -------------------------
    def _create_bars(self):
        for i in range(self.bar_count):
            bar = self.ax.barh(
                y=self.y_center,
                width=0,
                height=0.6,
                color=self.colors[i],
                left=i * (100 / self.bar_count)
            )
            self.bars.append(bar)

    # -------------------------
    # Configure plot view
    # -------------------------
    def _setup_plot(self):
        self.y_center = 0
        self.ax.set_title(self.title, fontsize=12, color="white", pad=5)
        self.ax.set_facecolor("#111")
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-1, 1)
        self.ax.set_yticks([])
        self.ax.set_xticks([])
        self._make_gradient()
        self._create_bars()

    # -------------------------
    # Set new simulated level
    # -------------------------
    def update_level(self):
        # Симуляция "двигающегося" уровня
        shift = random.randint(-5, 5)
        self.level = min(max(self.level + shift, 0), 100)

    # -------------------------
    # Draw level on screen
    # -------------------------
    def draw(self):
        active_bars = int((self.level / 100) * self.bar_count)
        for i in range(self.bar_count):
            w = (100 / self.bar_count) * 0.9
            if i < active_bars:
                self.bars[i][0].set_width(w)
            else:
                self.bars[i][0].set_width(0)


# ================================
#     Create figure + meters
# ================================
fig, axes = plt.subplots(
    2, 1, figsize=(10, 3),
    facecolor="#222"
)

meter_L = AudioMeter(axes[0], "L")
meter_R = AudioMeter(axes[1], "R")

# Start with random levels
meter_L.level = random.randint(20, 80)
meter_R.level = random.randint(20, 80)

# ================================
#        Animation update
# ================================
def animate(frame):
    meter_L.update_level()
    meter_R.update_level()

    meter_L.draw()
    meter_R.draw()
    return []

# ================================
#              RUN
# ================================
ani = animation.FuncAnimation(
    fig, animate, interval=100, blit=True
)

plt.tight_layout()
plt.show()
