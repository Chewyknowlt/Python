# Pass function as parameter
lst = [1, 2, 3, 4]

#making function as map()
def my_map(func, list):
    return [func(n) for n in list]

#calling function
print(my_map(lambda n :  n**2, lst))
