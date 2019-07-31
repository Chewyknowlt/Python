from PIL import Image
import os, shutil

def change_size_extension(lenngth = 200, breadth = 200, location = None):
    '''To resize image.'''
    # pdb.set_trace()
    size = (length, breadth)   #-> 200,200
    if location == '':
        location = r'B:\Python Course Program\Ch21_imageManupulation_pillow_module_PIL\New folder'
        print(location)
        for item in os.listdir(location):   # location= '' -> current location
            img = Image.open(item)  #making image obj & load it to memory
            print(item)
            if not img.thumbnail(size):   #Compare size of image
                img.thumbnail(size)    #Change size of image
                img.save(f'{item}')    
            # [i for i in os.listdir if i[-3:] in ['PNG', 'PEG', 'JPG', 'IFT', 'BMP, GIF']]
#prompting
path = input(r'Enter Path(for current path directly enter):  ')
length = float(input("Enter length(by Defalut= 200): "))
breadth = float(input("Enter breadth(by Defalut= 200): "))
# LST = [i for i in os.listdir(r'B:\Python Course Program\Ch21_imageManupulation_pillow_module_PIL\New folder') if i[-3:] in ['PNG', 'PEG', 'JPG', 'IFT', 'BMP, GIF']]
# print(os.getcwd())
change_size_extension(length, breadth, path)
# print(LST)
# a = os.walk( r'B:\Python Course Program\Ch21_imageManupulation_pillow_module_PIL\New folder')
# for p, fol, fil in a:
#     print(f'path: {p}')
#     print(f'folder: {fol}')
#     print(f'File: {fil}')