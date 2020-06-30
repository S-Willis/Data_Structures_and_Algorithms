from PIL import Image

class SeamCarving():

    def __init__(self,image):
        self.image = Image.open(image)
        self.image_width = self.image.size[0]
        self.image_height = self.image.size[1]
        self.rgb_image = self.image.convert('RGB')
        self.image_array = [[self.rgb_image.getpixel((x,y)) for x in range(self.image_width)] for y in range(self.image_height)]

if __name__ == '__main__':
    test = SeamCarving('./cat.jpg')
