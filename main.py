import matrix
import coder
import numpy as np # type: ignore
from PIL import Image

#while True:
#    i = input()
#    if i == "p":
#        target = (int(input()), int(input()), int(input()))
#        print(matrix.post_coords(target))
#    elif i == "g":
#        target = str(input())
#        print(matrix.get_coords(target))

def open_image(path):
        img = Image.open(path)
        img.convert('RGB')
        return img 

def image_to_data(img):
    pix = np.array(img)
    return pix.reshape(-1, 3)

def encode(text, path):
    data = []
    for char in text:
         data.append(matrix.get_coords(char))
    img = open_image(path)
    pix = image_to_data(img)
    height, width = img.size    
    colors = coder.encoder.encode(data, height, width, pix)
    new_img = Image.new('RGB', (width*2, height*2))
    pixels = new_img.load()
    for y in range(height):
        for x in range(width):
            pixels[x*2, y*2] = next(colors)
            pixels[x*2+1, y*2] = next(colors)
            pixels[x*2, y*2+1] = next(colors)
            pixels[x*2+1, y*2+1] = next(colors)
    new_img.save('encoded.png')

encode(str(input()), str(input()))