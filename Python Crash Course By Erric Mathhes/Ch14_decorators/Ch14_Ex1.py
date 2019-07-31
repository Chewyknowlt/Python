# decorator ->return name, doc, time 

from functools  import wraps  #To read docstring&name of org f()
import time #cal executable time

def time_decorator(function): #Decorator
    '''This is time decorator'''
    @wraps(function) #calling wraps to redirects to org f()
    def wrapper(*args, **kwargs):
        print(f'Function: {function.__name__}') #f()-> name
        print(f'Docstrings: {function.__doc__}') #Docstring-> name
        t1 = time.time() # time before execution
        returnable = function(*args, **kwargs) #calling req. function
        t2 = time.time() #time after execution
        print(f'Time: {t2-t1}s') # final time
        return returnable
    return wrapper

@time_decorator  #Apply decorators
def add(*args): 
    '''add() takes n no. of args & return there sum.'''
    return sum(args)

print(add(4, 5))