# make fun() which takes list as argument 
#  sqr. each element of the list 

def square_list(list):
    return  [x**2 for x in list]

numbers = [1, 2, 3, 4]
print(square_list(numbers))