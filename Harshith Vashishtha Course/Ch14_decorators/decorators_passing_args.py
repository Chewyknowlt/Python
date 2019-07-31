def only_dataType_allow(dataType, dataType2 = None):
    def decorators(function):
        def wrapper(*args, **kwargs):
            data = [type(arg) == dataType or type(arg) == dataType2 for arg in args] #[True, False, True]
            if all(data): # list -> all true
                return function(*args, **kwargs)
            return 'Invalid argument '
        return wrapper
    return decorators

@only_dataType_allow(int, float)
def add(*args):
    '''This is adder'''
    return sum(args)

print(add(1,2,3,4.0))       #perfect input
# print(add(1,2,3,4.0, []))   #falty input
