# this module redirects to f() as before decorators
from functools import wraps 

def decorator_func(any_function): #decorator function
    '''this is decorator'''
    @wraps(any_function) #redirects to org to read docstrings
    def wrapping_func(*args, **kwargs): # agrs+ kwrags pass
        print('This is decorator function') #do what we want before calling
        return any_function(*args, **kwargs) # calling function with args +kwargs
    return wrapping_func

@decorator_func  #calling decorator
def f(a, b):
    '''Add two args ''' # docstrings
    return a+b

print(f(5, 4))
print(f.__doc__) # read org docstrings
print(f.__name__) #read org name