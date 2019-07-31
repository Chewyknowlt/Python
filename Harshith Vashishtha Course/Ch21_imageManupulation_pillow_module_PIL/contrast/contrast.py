from PIL import Image, ImageEnhance

image = Image.open('1.jpg')
enhancer = ImageEnhance.Contrast(image)
for i in range(-10, 11):
  enhancer.enhance(i).save(f'1_{i}.jpg')

# -1 & beyond -> infrared (redish)
# 0 -> nothiing to show
# 1 -> original
# 2 & beyond -> ultra contrast (bluish)