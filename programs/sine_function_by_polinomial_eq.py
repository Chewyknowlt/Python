# sin(x) = 1 - (x^2/2!) + (x^3/3!) -.....
# where x in radian, sin(30) = sin(0.5235987756) = 0.5 approx.
# it is giving some error 

def factorial(sequence):
    #Making factorial of x
    f_a = sequence 
    while (sequence != 1):
        if (sequence != 1):
            sequence = sequence-1
            f_a = f_a * sequence
    return f_a

def power(x):
    #Making power
    x =  x ** sequence
    return x

x = float(input('Enter no. to evaluate of sin(x) where x in radian: '))
iteration = 1
sequence = 2
edit = []

while iteration != 100:
    term = power(x)/factorial(sequence)
    if (sequence % 2) == 0:
        term = term * -1
        edit.append(term)
    
    elif (sequence % 2) != 0:
        edit.append(term)
    iteration += 1
    sequence += 1

answer = sum(edit)
answer = 1 - answer
print('sin(x) = ' + str(answer))


    





