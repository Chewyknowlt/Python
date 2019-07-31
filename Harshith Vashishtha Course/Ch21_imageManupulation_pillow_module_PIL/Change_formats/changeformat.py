from PIL import Image
import os

def changeFormat(format= ''):
    path  = r'/media/hamza/linux/Coding/Pyhton/Python_Harshit_Vashishtha/Python Course Program/Ch21_imageManupulation_pillow_module_PIL/Change_formats'
    print(path)
    l = [i for i in os.listdir(path) if i[-3:].upper() in ['JPEG', 'JPG', 'PNG']]
    print(l)
    for i in l:
        if not i.endswith(format):
            print(i[-3:])
            image = Image.open(i)
            print(i)
            fileName, ext = os.path.splitext(i)
            image.save(f'{fileName}{format}')
        return None

changeFormat('.jpeg')
