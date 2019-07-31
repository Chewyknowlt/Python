from PIL import Image, ImageDraw,ImageFont

image = Image.open('3.jpg')#to open image
draw = ImageDraw.Draw(image) #drawing text oon image
# myFont = ImageFont.truetype("arail.ttf", 50)
points = 100,100
write = 'she is super hot'

draw.text(points, write, "white")
image.save('texted.jpg')