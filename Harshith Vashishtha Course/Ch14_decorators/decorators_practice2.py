# decorator -> return name, doc, time, Check proper input

from functools import wraps #To read docstring&name of org f()
import time #cal executable time

def master_decorators(function): #Decorator
    '''This is master decorator'''
    @wraps(function) #calling wraps to redirects to org f()
    def wrapper(*args, **kwargs):
        print(f'Function: {function.__name__}') #f()-> name
        print(f'Docstring: {function.__doc__}') #Docstring-> name
        data = [type(arg) == int or type(arg) == float for arg in args] #[True, False, True]
        if all(data): # list -> all true
            t1 = time.time() # time before execution
            returnable = function(*args, *kwargs)
            t2 = time.time() #time after execution
            print(f'Time: {t2-t1}s') # final time
            return returnable
        else: 
                return 'Wrong Input'
    return wrapper
    
@master_decorators #Apply decorators
def add(*args):
    '''This is adder'''
    return sum(args)

print(add(1,2,3,4.0))       #perfect input
# print(add(1,2,3,4.0, []))   #falty input
