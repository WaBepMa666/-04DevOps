# 1. Генератор 4 случайных байт с переключателями (NRZ кодирование)
import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("32-битный генератор (4 байта)")
root.geometry("500x400")

bytes_data = [[random.randint(0, 1) for _ in range(8)] for _ in range(4)]
bin_str = ''.join(''.join(map(str, row)) for row in bytes_data)
hex_str = hex(int(bin_str, 2))[2:].upper().zfill(8)
check_sum = sum(sum(row) for row in bytes_data)


def update_bytes():
    global bytes_data, bin_str, hex_str, check_sum
    bytes_data = [[random.randint(0, 1) for _ in range(8)] for _ in range(4)]
    bin_str = ''.join(''.join(map(str, row)) for row in bytes_data)
    hex_str = hex(int(bin_str, 2))[2:].upper().zfill(8)
    check_sum = sum(sum(row) for row in bytes_data)
    draw_switches()
    lbl_bin.config(text=f"Binary: {bin_str}")
    lbl_hex.config(text=f"Hex: 0x{hex_str}")
    lbl_sum.config(text=f"CheckSum: {check_sum} (0x{hex(check_sum)[2:].upper()})")


def flip_switch(byte_idx, bit_idx):
    bytes_data[byte_idx][bit_idx] = 1 - bytes_data[byte_idx][bit_idx]
    draw_switches()


def draw_switches():
    for widget in frame_switches.winfo_children():
        widget.destroy()

    for b in range(4):
        tk.Label(frame_switches, text=f"Byte {b + 1}").grid(row=b, column=0, columnspan=9)
        for bit in range(8):
            var = tk.IntVar(value=bytes_data[b][bit])
            chk = tk.Checkbutton(frame_switches, variable=var, width=2,
                                 command=lambda bb=b, bi=bit: flip_switch(bb, bi))
            chk.grid(row=b, column=bit + 1, padx=1)


frame_switches = tk.Frame(root)
frame_switches.pack(pady=10)

lbl_bin = tk.Label(root, text="Binary: ", font=("Courier", 10))
lbl_bin.pack()
lbl_hex = tk.Label(root, text="Hex: ", font=("Courier", 10))
lbl_hex.pack()
lbl_sum = tk.Label(root, text="CheckSum: ", font=("Courier", 12, "bold"))
lbl_sum.pack()

tk.Button(root, text="Новый рандом", command=update_bytes, bg="lightblue").pack(pady=10)
update_bytes()
root.mainloop()
