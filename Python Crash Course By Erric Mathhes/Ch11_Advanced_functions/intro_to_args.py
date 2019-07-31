# multimple arguments can be passed  through *args
# *args  is not special key word we can use anything but this is standard
# e.g; *args  supersede of *add of anything

def adder(*args):
    total = 0
    for num in args:
        total += num
    print(type(args))  #this *args makes tuple
    return total

print(adder(5,6,4))