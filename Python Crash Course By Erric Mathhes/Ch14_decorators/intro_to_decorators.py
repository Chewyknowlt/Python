#enhance functionality of other functions without changing their code
def decorator_func(any_function): #decorator function
    def wrappin_func():
        print('This is decorator function') #do what we want before calling
        any_function() # calling function
    return wrappin_func

def func1(): #Ex: 1 -> var as obj
    print('This is func 1')
var = decorator_func(func1)
var()

def func2(): # Ex2: -> use f() name as obj
    print('This is func 2')
func2 = decorator_func(func2)
func2()

@ decorator_func #Ex3: Calling decorator with @ short cut
def func3():
    print('This is func 3')
func3()