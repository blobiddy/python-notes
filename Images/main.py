import os
from PIL import Image, ImageFilter, ImageEnhance

path = './imgs'
pathout = './imgsout'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(180)
    factor = 5
    enhancer = ImageEnhance.Contrast(edit)
    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathout}/{clean_name}.png")
