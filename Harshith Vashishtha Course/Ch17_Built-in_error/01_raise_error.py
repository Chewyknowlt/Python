def add(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a+b
    return TypeError('Entered wrong data type')

print(add(1, 2)) #work fine
print(add('1', '2')) #raise TypeError