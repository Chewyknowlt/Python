from PIL import Image, ImageEnhance
import os 

image = Image.open('dog.png')
enhancer = ImageEnhance.Sharpness(image)
enhancer.enhance(10).save('dog_extremeSharp.jpg')
#below 0 blury
# 0 : blurry 
# 1: original image 
# 2 : image with increased sharpness 