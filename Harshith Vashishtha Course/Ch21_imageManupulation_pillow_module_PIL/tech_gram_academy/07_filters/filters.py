from PIL import Image, ImageFilter

image = Image.open('2.jpg')
image.filter(ImageFilter.EMBOSS).show()
image.save('EMBOSS.jpg')
del image
# .BLUR filter
# .BoxBLur(arg) 0-100
# .CONTOUR
# .EDGE_ENHANCE
# .EDGE_ENHANCE_MORE
# .MaxFilter
# .SHARPEN
# .SMOOTH_MORE