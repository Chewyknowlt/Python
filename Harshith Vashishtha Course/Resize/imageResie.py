from PIL import Image
import os, pdb

# pdb.set_trace()
def image_resize(length=200, width=200):
    # pdb.set_trace()
    size = (length, width)
    path = os.getcwd() 
    lst = [i for i in os.listdir(path) if i[-3:].upper() in ['PEG', 'JPG', 'PNG']]
    print(lst)
    for item in lst:
        print(item)
        image = Image.open(item)
        if not image.thumbnail(size):
            image.thumbnail(size)
            image.save(item)
    return None

image_resize()