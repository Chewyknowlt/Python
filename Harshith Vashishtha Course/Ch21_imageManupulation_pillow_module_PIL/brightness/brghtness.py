from PIL import Image, ImageEnhance
import os

# --------brightness -----------
image = Image.open('1.jpg')
enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(10).save('1_10.jpg')

# 0 & beyond -> black
# 1 & above -> brightness