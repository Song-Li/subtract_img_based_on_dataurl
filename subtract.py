import numpy as np
from PIL import ImageChops
from PIL import Image
import re
import base64
import cStringIO

def get_picture(image_b64):
    # remove the define part of image_b64
    image_b64 = re.sub('^data:image/.+;base64,', '', image_b64)
    # decode image_b64
    image_data = image_b64.decode('base64')
    image_data = cStringIO.StringIO(image_data)
    image_PIL = Image.open(image_data)
    return image_PIL

def subtract(img1, img2, scale = 1, offset = 0):
    img1 = img1.convert('RGB')
    img2 = img2.convert('RGB')
    img1.save('./img1.png', 'png')
    img2.save('./img2.png', 'png')
    diff = ImageChops.difference(img1, img2)
    print diff.getbbox()
    return ImageChops.subtract(img1, img2, scale, offset)

def do_subtract():
    file_1 = './1.dat'
    file_2 = './2.dat'
    str_1 = ""
    str_2 = ""
    with open(file_1) as f1:
        str_1 = f1.read()
    with open(file_2) as f2:
        str_2 = f2.read()
    img1 = get_picture(str_1)
    img2 = get_picture(str_2)
    res = subtract(img1, img2, scale = 0.01)
    res.save('res1.png', 'png')
    res = subtract(img2, img1, scale = 0.01)
    res.save('res2.png', 'png')

if __name__ == '__main__':
    do_subtract()
