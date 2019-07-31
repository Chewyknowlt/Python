#install library -> pip install Pillow

from PIL import Image
import os

# img1 = Image.open('1.jpg') #open file as obj

# #Change image extension
# img1.save('1.pdf')  #To change format

# #Loop to change image extension
# convert_format = '.jpeg'  # desired extension to convert
# path = r'B:\Python Course\Ch21_imageManupulation_pillow_module_PIL' #path of file execution
# for item in os.listdir(path):  #os.listdir()  ->list of current dir
#     if not item.endswith(convert_format): # NOT desireable extension
#         img =  Image.open(item)  #creting image obj
#         fileName, extension = os.path.splitext(item) #split <name> <.extension>    
#         img.save(f'{ fileName }{ convert_format }')

# #show image
# img1.show('dog.png') #to show image

# #Resize image
# max_size = (250, 250)
# img1.thumbnail(max_size)
# img1.save('dog1_resized.jpeg')

# Loop to resize image
# convert_extension = '.jpeg'
size_img = (200,200)
# path = r'B:\Python Course\Ch21_imageManupulation_pillow_module_PIL'
for item in os.listdir():
    img = Image.open(item)
    if not img.thumbnail(size_img):
        img.thumbnail(size_img)
        fileName, extension = os.path.splitext(item) #split <name> <.extension>    
        # img.save(f'{fileName}{convert_extension}')
        img.save(f'{item}')