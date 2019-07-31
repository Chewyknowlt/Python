from PIL import Image

# L ->gray scale, 8bit
# RGB -> red, green & blue -> 3byte, 
# image = Image.new('RGB', size) -> black
# image = Image.new('RGB', size, 'white') -> white
# image = Image.new('RGB', size, '#ffff') -> white
# image = Image.new('RGB', size, 'rgb(0%, 100%, 0%)') -> green
# RGBA ->red, green & blue -> 
# CMYK -> BLACK & YELLOW -> 4BITS
# YCbCr ->
# F -> 32 bits int and float

size = length, breadth = 320, 240
image = Image.new('L', size, 'hsl(0%, 100%, 50%)')
image.save('F.png')