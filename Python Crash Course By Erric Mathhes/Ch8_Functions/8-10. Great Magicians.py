print('8-10. Great Magicians')

# Putting working objects ionto empty lst. 
def make_great(megicians):
    while megicians:
        current_megician = megicians.pop()
        print('I\'m considering ' + current_megician)
        mod_megicians.append(current_megician)
    print()

# Append to mod. lst.
def new_magicians(more_megicians):
    while more_megicians:
        current_magician = more_megicians.pop()
        print(current_magician.title() + ' is also good.')
        mod_megicians.append(more_megicians)
    print()

# To show
def show_magicians(mod_megicians):
    for magician in megicians:
        print(magician + ' is my favourite.')
    print()
    
#Working lst.
megicians = ['teller', 'penn', 'apollo', 'david']
mod_megicians = []
more_megicians = ['Shin', 'Lance']
#Call func.
make_great(megicians[:])
show_magicians(megicians[:])
new_magicians(more_megicians[:])

print(megicians)
print(mod_megicians)
print(more_megicians)
