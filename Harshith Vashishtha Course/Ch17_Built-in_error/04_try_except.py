# Exception handeling
#try, except
while True:  #run loop untill right input
    try:
        age = int(input("Enter age: ")) #six->go to except block
        break                               #otherwise break
    except ValueError:  # this errror we know -> we  handle it
        print('input in no.s . ')
    except:  # we handle this, but we dont know the error
        print('Unexpected Error!')
    
if age >= 18:
    print('You can play this game.')
else:
    print('You can play this game.')