from PIL import Image
import os

# img = Image.open('dog2.jpg')
size_img = (200,200)
#path = r'B:\Python Course\Ch21_imageManupulation_pillow_module_PIL'
for item in os.listdir():
        img = Image.open(item)
        img.thumbnail(size_img)
        print(item)
        img.save(item +'.jpeg')


