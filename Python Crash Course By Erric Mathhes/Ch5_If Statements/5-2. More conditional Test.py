print('5-2. More Conditional Test')

cars = ['audi','bmw','subaru','toyota']
speed = 20
velocity = 30
# 1st cond.
for car in cars:
    # Test for equality.
    if car.lower() == 'subaru' or car.lower() == 'bmw':
        print('This is my favourite car')
    # Test for inequality.
    elif car.lower() != 'subaru' or car.lower() != 'bmw':
        print('This car is not my favourite')
    # greater or less than for numericals.
if speed <= 25 and velocity >= 25:
        print('Hola! I got my car.')
        
    
