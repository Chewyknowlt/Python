print('8-9. Magicians')

#method 1.

# To show megicians.
def show_magicians(megicians):
    #Usinig for loop.
    for megician in megicians:
        print(megician.title() + ' is my favourite megician.')

#Working lst.
megicians = ['teller', 'penn', 'apollo', 'david']
#Call func.
show_magicians(megicians[:])
