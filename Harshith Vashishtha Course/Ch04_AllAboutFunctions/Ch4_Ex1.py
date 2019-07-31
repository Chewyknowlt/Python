# def func. takes 2 inputs from user and return greater 1
def greater(a, b):
    if a > b : return  a
    return b

def greatest(a, b, c):
    if b < a > c : return a # a > b and a > c
    elif  a < b > c : return b # b > a and b > c
    return c

def new_greatest(a, b, c):
    # bigger = greater(a, b)
    return greater(greater(a, b), c)
print(new_greatest(20, 30, 10))