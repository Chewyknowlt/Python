# to_power(3, *nums)
#input -> [1, 2, 3]
# output -> [1 , 8, 27]

def iterable_power(power, *args):
    if args :  return [(num ** power) for num in args]
    else: return  'Parse no data'

#Working with list                    
lst = [1, 2, 3, 4, 5]
print(iterable_power(2, *lst))           

#Working with tuple
tupl = (1, 2, 3, 4, 5)
print(iterable_power(2, *tupl))

#Exceptional case
print(iterable_power(2))
