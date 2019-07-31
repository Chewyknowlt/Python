from PIL import Image
import os

def changeFormat(format= ''):
    path  = os.getcwd()
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