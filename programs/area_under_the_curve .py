def f(variable):
    #It satisfying point in equation.
    x = variable
    f_x = eval(equation)
    return f_x

def summation_middle():
    # 2∑ fx , i = 1, n = n-1  
    fn = 0
    box_a = a
    while (box_a < b):
        fbox_a = f(box_a)
        fn += fbox_a
        box_a += width
    fn *= 2
    return fn

# from user.
equation = input('Enter equation: ') # ' (4*(x**2))+6 '
a = int(input('Enter point a: ')) # a = 2
b = int(input('Enter point b: ')) # b = 3
n = int(input('Enter no. of n: ')) # any
while (n == 0):
    n = int(input('Enter no. of n: '))

# Calculations.
width = (b-a)/n
length = f(a) + summation_middle() + f(b)
answer = width * 0.5 * length
if (answer < 0):
    answer *= -1

print(answer) # answer ~= 31.333339715878765 after 1 crore iterations.

