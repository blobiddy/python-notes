from PIL import Image

img = Image.open('balloon.png')
print(img.getbands())
