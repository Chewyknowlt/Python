print('7-6. Three Exits')

ask = input('Are you intrested to watch movie? (y/n)')
active = True
while active:
    if ask == 'y':
        age = int(input('How many old are you?'))
        if age <= 3:
            print('Yiur ticket is free.')
        
        elif age > 3 and age <= 12:
            print('Your ticket price is $10/= ')
        
        else:
            print('Your ticket price is $15/= ')
        active = False 
    else:
        break

