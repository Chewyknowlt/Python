# Function: add
#Docstring: add() takes n no. of args 
# & return there sum.
#output->  9
 
 #To read docstring&name of org f()
from functools import wraps 

def decorator(function):  #Decorator
    '''This is decorator function'''
    @wraps(function)  #calling wraps to redirects to org f()
    def wrapper(*args, **kwargs):
        print(f'Function: {function.__name__}') #f()-> name
        print(f'Docstring: {function.__doc__}') #Docstring-> name
        return function(*args, *kwargs)
    return wrapper

@decorator
def add(*args): 
    '''add() takes n no. of args & return there sum.'''
    return sum(args)

print(add(4, 5))