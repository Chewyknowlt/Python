from PIL import Image

# image = Image.open('thumbnail.jpg')
# logo = Image.open('converted_logo.png')
# image_copy = image.copy()
# pos = ((image_copy.width - logo.width), (image_copy.height - logo.height))
# image_copy.paste(logo, pos, logo)
# image_copy.save('pasted.jpg')
# image_copy.show()

logo = Image.open('resize.jpg')
converted_logo = logo.convert('L')
converted_logo.save('converted_resize.jpg')