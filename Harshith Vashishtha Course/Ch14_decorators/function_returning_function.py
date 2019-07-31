def outer():
    def inner():
        print("inside innner func")
    return  inner()  #callling here
# no need to make it object
outer()

def outer_func(msg):
    def inner_func():
        print(f"inner_func: {msg}")
    return inner_func #Not clling here

#making f() as obj 
var = outer_func("Hi")
var() 