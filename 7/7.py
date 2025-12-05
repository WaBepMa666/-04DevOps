# 7. Переводчик кодировок
import tkinter as tk
from tkinter import ttk
import base64

root = tk.Tk()
root.title("Кодировки текста")
root.geometry("500x400")

encodings = ['utf-8', 'cp1251', 'koi8-r', 'ascii', 'latin-1']
current_enc = tk.StringVar(value='utf-8')

text_area = tk.Text(root, height=8, width=50)
text_area.pack(pady=10)
text_area.insert('1.0', 'Привет, мир!')


def convert_encoding():
    text = text_area.get('1.0', tk.END).strip()
    result = ""

    try:
        bytes_data = text.encode(current_enc.get())
        bin_str = ' '.join(f'{b:08b}' for b in bytes_data)
        hex_str = bytes_data.hex().upper()
        b64 = base64.b64encode(bytes_data).decode()

        result = f"Кодировка: {current_enc.get()}\n"
        result += f"Bytes: {bytes_data}\n"
        result += f"Binary: {bin_str}\n"
        result += f"Hex: {hex_str}\n"
        result += f"Base64: {b64}"
    except:
        result = "Ошибка кодировки!"

    output_area.delete('1.0', tk.END)
    output_area.insert('1.0', result)


combo_enc = ttk.Combobox(root, textvariable=current_enc, values=encodings)
combo_enc.pack()
tk.Button(root, text="Конвертировать", command=convert_encoding).pack(pady=5)

output_area = tk.Text(root, height=10, width=60)
output_area.pack(pady=10)
convert_encoding()
root.mainloop()
