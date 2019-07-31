from PIL import Image

image = Image.open('1.jpg')
rotate_img = image.rotate(45).show()
rotate_img.save('new_1.jpg')