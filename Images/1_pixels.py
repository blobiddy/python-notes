from PIL import Image

input = input('Please input filename')
try:
    img = Image.open('dragonfly.png')
    pixels = img.width * img.height

    print('Fle name: ' + input)
    print(str(pixels) + ' pixels!')
except:
    print("File not found")
