from PIL import Image

img1 = Image.open('1.png')
img2 = Image.open('2.png')
# size = (200, 200)
# img1.thumbnail(size)
# img1.save('n1.jpg')
# img2.thumbnail(size)
# img2.save('n2.jpg')

# area = (0,50,50,50)
# crop1 = img1.crop(area).save('c1.png')
# crop2 = img1.crop(area).save('c2.png')
Image.blend(img1, img2, 0.5).save('blended.png')
# 0,80,150,80