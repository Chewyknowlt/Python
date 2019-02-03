print('8-3. T-Shirt')

def make_shirt(size, text):
    #Displaying size and text of shirt.
    print('Size of shirt: ' + size.title())
    print('Text on shirt: ' + text)
    print()
# Positional Argument.
make_shirt('large', 'LoveU')

# Keyword Argument.
make_shirt(text = 'Hola!', size = 'medium')



