import matrix
import coder
import numpy as np
from PIL import Image

def open_image(path):
    return Image.open(path).convert("RGB")

def image_to_data(img):
    pix = np.array(img)
    return pix.reshape(-1, 3)

def encode(text, path):
    data = []
    for char in text:
        coords = matrix.get_coords(char)
        if coords is not None:
            data.append(coords)

    img = open_image(path)
    pix = image_to_data(img)
    width, height = img.size    

    enc = coder.Encoder()
    colors = enc.encode(data, height, width, iter(pix))

    new_img = Image.new("RGB", (width*2, height*2))
    pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            pixels[x*2,   y*2]   = next(colors)
            pixels[x*2+1, y*2]   = next(colors)
            pixels[x*2,   y*2+1] = next(colors)
            pixels[x*2+1, y*2+1] = next(colors)

    new_img.save("encoded.png")

encode(str(input("Текст: ")), str(input("Шлях до картинки: ")))
