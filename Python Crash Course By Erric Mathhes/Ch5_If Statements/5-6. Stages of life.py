print('5-6. Stages of Life')

# Using if-elif- else chain.
age = int(input("Enter your age: "))
if age < 2:
    print('Person is baby.')
elif age == 2 or age < 4:
    print('Person is Todler.')
elif age == 4 or age < 13:
    print('Person is kid.')
elif age == 13 or age < 20:
    print('Person is teenager.')
elif age == 20 or age < 65:
    print('Person is adult.')
else:
    print('Peson is older.')
