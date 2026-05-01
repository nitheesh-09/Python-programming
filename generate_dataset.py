import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

os.makedirs("dataset", exist_ok=True)

font = ImageFont.load_default()

for ch in chars:
    folder = f"dataset/{ch}"
    os.makedirs(folder, exist_ok=True)

    for i in range(200):
        img = Image.new("L", (28, 28), color=255)
        draw = ImageDraw.Draw(img)
        draw.text((8, 5), ch, fill=0, font=font)

        arr = np.array(img)
        cv2.imwrite(f"{folder}/{i}.png", arr)

print("Dataset created!")
