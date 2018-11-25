#Practice Problem 3.3

##Translate these into Python if/else statements:

###(a) If year is divisible by 4, print 'Could be a leap year.'; otherwise print 'Definitely nota leap year.'
leap_year = (366)

if leap_year % 4:
    print('It is a leap year.')
else:
    print('It is not a leap year. ')


###(b) If list ticket is equal to list lottery, print 'You won!'; else print 'Better luck nexttime...'
ticket = input('Enter code: ')
lottery = ['10', '30', '50']

if ticket in lottery:
    print('You won.')
else:
    print('Better luck next time.')


    
