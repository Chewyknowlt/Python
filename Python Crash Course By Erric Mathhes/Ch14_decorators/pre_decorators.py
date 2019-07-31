# variable assigned to function points same location
def sqr(a):
    return a**2

#points towards position of memory
s = sqr

#org. f() name
print(s.__name__)
print(sqr.__name__)
 
#Memory location
print(s)
print(sqr)