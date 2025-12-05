# 9. Влияние искажений на текст (Bit Flip)
import tkinter as tk
from tkinter import ttk
import binascii

root = tk.Tk()
root.title("Искажения на битовом уровне")
root.geometry("600x500")

text_var = tk.StringVar(value="Привет, мир!")
bit_errors = tk.IntVar(value=0)

tk.Label(root, text="Исходный текст:", font=("Arial", 12, "bold")).pack(pady=5)
tk.Entry(root, textvariable=text_var, width=40, font=("Courier", 10)).pack(pady=5)

tk.Label(root, text="Количество ошибок:").pack()
error_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, variable=bit_errors)
error_scale.pack(pady=10)

result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True, pady=10)


def corrupt_text():
    text = text_var.get()
    try:
        # Кодируем в UTF-8
        bytes_data = text.encode('utf-8')
        bit_str = ''.join(f'{b:08b}' for b in bytes_data)

        # Добавляем ошибки
        bits_list = list(bit_str)
        error_pos = sorted(random.sample(range(len(bits_list)), bit_errors.get()))
        for pos in error_pos:
            bits_list[pos] = '1' if bits_list[pos] == '0' else '0'

        corrupted_bits = ''.join(bits_list)
        corrupted_bytes = [int(corrupted_bits[i:i + 8], 2) for i in range(0, len(corrupted_bits), 8)]
        corrupted_text = bytes(corrupted_bytes).decode('utf-8', errors='replace')

        orig_label.config(text=f"Оригинал: {text}")
        corr_label.config(text=f"Искажено: {corrupted_text}")
        bits_label.config(text=f"Изменено бит: {bit_errors.get} в позициях {error_pos}")

    except:
        orig_label.config(text="Ошибка декодирования!")


orig_label = tk.Label(result_frame, text="Оригинал: ", font=("Courier", 11), bg='lightgreen')
orig_label.pack(anchor='w')
corr_label = tk.Label(result_frame, text="Искажено: ", font=("Courier", 11), bg='lightcoral')
corr_label.pack(anchor='w')
bits_label = tk.Label(result_frame, text="", font=("Courier", 10), fg='blue')
bits_label.pack(anchor='w')

tk.Button(root, text="Применить искажения", command=corrupt_text).pack(pady=10)
corrupt_text()
root.mainloop()
