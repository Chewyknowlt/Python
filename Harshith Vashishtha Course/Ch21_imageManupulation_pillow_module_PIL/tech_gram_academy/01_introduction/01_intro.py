from PIL import Image

img = Image.open('python.jpeg')

print(img.height)
print(img.width)
print(img.size)
print(img.format)