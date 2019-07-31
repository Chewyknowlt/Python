from PIL import Image, ImageEnhance, ImageFilter
import os

image = Image.open('1_1.jpg')
myfilter = ImageFilter.GaussianBlur()
image.filter(myfilter).save('1_1.jpeg')