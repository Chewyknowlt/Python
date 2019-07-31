# 0 1 1 2 3 5 8 13.....

def fabonacci(number):
    a = 0
    b = 1
    if number == 1: print(a)
    elif number == 2: print(a, b, end = ", ")
    else:
        print(a, b, end = ", ")
        for i in range(number-2):
            c = a + b 
            a = b
            b = c
            print(b, end = ", ")

fabonacci(10)