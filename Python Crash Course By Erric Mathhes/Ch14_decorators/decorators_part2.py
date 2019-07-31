def decorator_func(any_function): #decorator function
    def wrapping_func(*args, **kwargs): # agrs+ kwrags pass
        print('This is decorator function') #do what we want before calling
        return any_function(*args, **kwargs) # calling function with args +kwargs
    return wrapping_func

@decorator_func  #calling decorator
def f(a, b):
    return a+b
print(f(5, 4))

