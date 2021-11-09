
from PIL import Image
from pyzbar.pyzbar import decode

def decode_img(img):
    result = decode(Image.open(img))
    # print(result)
    return result