#args as parameter and argument
def adder(*args):
    total = 0
    for n in args : total += n
    return total

#Working with list
lst = [1, 2 ,3 ,4 ,5]
print(adder(*lst)) #   *lst -> unpack its element

#Working with tuple
tupl = (1, 2 ,3 ,4 ,5)
print(adder(*tupl)) # *tupl -> unpack its element