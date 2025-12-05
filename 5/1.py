import flet as ft

def main(page: ft.Page):
    page.title = "Термометр"
    page.bgcolor = "#11141b"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # параметры диапазона температур
    t_min, t_max = -40, 50

    # текст с текущей температурой
    value_text = ft.Text("0 °C", size=30, color="white", weight=ft.FontWeight.BOLD)

    # фон шкалы
    scale_bg = ft.Container(
        width=40,
        height=220,
        bgcolor="#222831",
        border_radius=20,
        padding=4,
    )

    # цветной столбик (уровень “ртути”)
    mercury = ft.Container(
        width=scale_bg.width - 8,
        height=0,                  # будем менять
        bgcolor="#ff5252",
        border_radius=20,
        alignment=ft.alignment.bottom_center,
    )

    # контейнер, в который кладём столбик
    mercury_holder = ft.Container(
        width=scale_bg.width - 8,
        height=scale_bg.height - 8,
        bgcolor="#151920",
        border_radius=20,
        content=ft.Column(
            [mercury],
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        ),
    )

    # метки по краю (текст)
    label_min = ft.Text(f"{t_min} °C", color="#90caf9", size=12)
    label_mid = ft.Text("0 °C", color="#90caf9", size=12)
    label_max = ft.Text(f"{t_max} °C", color="#90caf9", size=12)

    # функция обновления уровня
    def set_temp(val: float):
        # clamp
        v = max(t_min, min(t_max, val))
        # нормализуем 0..1
        k = (v - t_min) / (t_max - t_min) if t_max != t_min else 0
        max_h = mercury_holder.height - 4
        mercury.height = max_h * k

        # цвет в зависимости от температуры
        if v <= 0:
            mercury.bgcolor = "#40c4ff"   # синий
        elif v < 25:
            mercury.bgcolor = "#ffca28"   # жёлтый
        else:
            mercury.bgcolor = "#ff5252"   # красный

        value_text.value = f"{int(v)} °C"
        page.update()

    # слайдер управления
    slider = ft.Slider(
        min=t_min,
        max=t_max,
        value=0,
        divisions=(t_max - t_min),
        width=260,
        label="{value} °C",
        on_change=lambda e: set_temp(float(e.control.value)),
    )

    # стартовое значение
    set_temp(0)

    page.add(
        ft.Column(
            [
                value_text,
                ft.Row(
                    [
                        # шкала с ртутью
                        ft.Stack(
                            [
                                scale_bg,
                                ft.Container(
                                    content=mercury_holder,
                                    alignment=ft.alignment.center,
                                ),
                            ],
                            width=scale_bg.width,
                            height=scale_bg.height,
                        ),
                        # подписи рядом
                        ft.Column(
                            [
                                label_max,
                                ft.Container(height=scale_bg.height/2 - 20),
                                label_mid,
                                ft.Container(height=scale_bg.height/2 - 20),
                                label_min,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16,
                ),
                slider,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)
