def f():
    #satisfy any expression with 2 points.
    eq = input('Enter expression here not equation whose variable must be in "x":\n')
    a = float(input('Enter point 1: '))
    x = a
    ans_1 = eval(eq)
    b = float(input('Enter point 2: '))
    x = b
    ans_2 = eval(eq)
    return ans_1, ans_2

#applying function.
test = f()          # (x**2) - 5*x + 6 , s.s = {2,3}
print(test)
