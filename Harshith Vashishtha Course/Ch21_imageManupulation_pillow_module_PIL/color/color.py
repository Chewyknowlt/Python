from PIL import Image, ImageEnhance

image = Image.open('1.jpg')
enhancer = ImageEnhance.Color(image)
enhancer.enhance(-10).save('1_-10.jpg')


# -1 & beyond -> infrared colors
# 0 -> black & white
# 1 & beyond -> sharp colors