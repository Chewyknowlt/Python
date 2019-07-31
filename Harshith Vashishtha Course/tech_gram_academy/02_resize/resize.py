from PIL import Image

img = Image.open('python.png')
size = (300, 300) #length, width
img.thumbnail(size) # .thumbnail((300,300))
img.save('py.png')

# size can be small but not large

