from PIL import Image
import numpy as np # type: ignore

class encoder():
    
    img = None

    def open_image(self, path):
        img = Image.open(path)
        img.convert('RGB')
        self.img = img
        return img 

    def image_to_data(self, img):
        app = np.array(img)
        return app

        
class decoder():
    pass