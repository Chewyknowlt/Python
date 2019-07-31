from PIL import Image

image = Image.open('n1.jpg')
#area = (x1, y1   ,x2,y2)
area = (0, 80, 150, 80)
image.crop(area)
image.save('new_n1.jpg')
# croped.show()
# croped.save('new_1.jpg')