# 3. Коды клавиш (ASCII, Unicode, CP1251, CP866)
import tkinter as tk

root = tk.Tk()
root.title("Коды символов")
root.geometry("400x300")

lbl_key = tk.Label(root, text="Нажмите клавишу", font=("Arial", 16))
lbl_key.pack(pady=20)

info_frame = tk.Frame(root)
info_frame.pack(pady=10)


def on_key(event):
    char = event.char or "[Spec]"
    ord_ascii = ord(char) if char != "[Spec]" else event.keycode
    unicode_val = ord(char) if char != "[Spec]" else event.keycode

    lbl_key.config(text=f"Клавиша: '{char}'")
    lbl_ascii.config(text=f"ASCII: {ord_ascii}")
    lbl_unicode.config(text=f"Unicode: U+{unicode_val:04X}")
    lbl_cp1251.config(text=f"CP1251: {ord_ascii}")
    lbl_cp866.config(text=f"CP866: {ord_ascii}")


lbl_ascii = tk.Label(info_frame, text="ASCII: ", font=("Courier", 12))
lbl_ascii.grid(row=0, column=0, sticky="w")
lbl_unicode = tk.Label(info_frame, text="Unicode: ", font=("Courier", 12))
lbl_unicode.grid(row=1, column=0, sticky="w")
lbl_cp1251 = tk.Label(info_frame, text="CP1251: ", font=("Courier", 12))
lbl_cp1251.grid(row=2, column=0, sticky="w")
lbl_cp866 = tk.Label(info_frame, text="CP866: ", font=("Courier", 12))
lbl_cp866.grid(row=3, column=0, sticky="w")

root.bind('<KeyPress>', on_key)
root.focus_set()
root.mainloop()
