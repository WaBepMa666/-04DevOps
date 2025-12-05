# 1. Искажение изображения с PSNR/SSIM
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
import random

root = tk.Tk()
root.title("Искажение изображений")
root.geometry("800x600")

error_rate = tk.DoubleVar(value=0.05)
original_img = None
distorted_img = None


def load_image():
    global original_img
    path = filedialog.askopenfilename(filetypes=[("Image", "*.png *.jpg *.jpeg")])
    if path:
        original_img = np.array(Image.open(path).convert('RGB'))
        show_images()


def corrupt_image():
    global distorted_img
    if original_img is None: return

    h, w, c = original_img.shape
    mask = np.random.random((h, w, c)) < error_rate.get()
    distorted_img = original_img.copy()
    distorted_img[mask] = np.random.randint(0, 256, distorted_img[mask].shape)
    show_images()


def calculate_metrics():
    if original_img is None or distorted_img is None: return
    p = psnr(original_img, distorted_img, data_range=255)
    s = ssim(original_img, distorted_img, multichannel=True, data_range=255)
    lbl_metrics.config(text=f"PSNR: {p:.2f} dB | SSIM: {s:.4f}")


def save_distorted():
    if distorted_img is not None:
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path: Image.fromarray(distorted_img.astype(np.uint8)).save(path)


def show_images():
    if original_img is not None:
        img1 = Image.fromarray(original_img).resize((250, 250))
        lbl_orig.config(image=ImageTk.PhotoImage(img1))
        lbl_orig.image = ImageTk.PhotoImage(img1)
    if distorted_img is not None:
        img2 = Image.fromarray(distorted_img).resize((250, 250))
        lbl_dist.config(image=ImageTk.PhotoImage(img2))
        lbl_dist.image = ImageTk.PhotoImage(img2)


tk.Button(root, text="Загрузить", command=load_image).pack(pady=5)
tk.Scale(root, from_=0, to=0.2, resolution=0.01, orient=tk.HORIZONTAL,
         variable=error_rate, label="% ошибок").pack(pady=5)
tk.Button(root, text="Искажение", command=corrupt_image).pack(pady=5)
tk.Button(root, text="Метрики", command=calculate_metrics).pack(pady=5)
tk.Button(root, text="Сохранить", command=save_distorted).pack(pady=5)

lbl_orig = tk.Label(root, text="Оригинал")
lbl_orig.pack(side=tk.LEFT, padx=20)
lbl_dist = tk.Label(root, text="Искаженное")
lbl_dist.pack(side=tk.RIGHT, padx=20)
lbl_metrics = tk.Label(root, text="PSNR/SSIM")
lbl_metrics.pack(pady=10)
root.mainloop()
