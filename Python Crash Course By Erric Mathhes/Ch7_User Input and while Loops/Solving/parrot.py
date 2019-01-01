prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter \'quit\' to end of program.'
'''
# Method 1
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
    
# Method 2
message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Method 3
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Breaking condition.
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('I\'d love to go to ' + city.title() + '!')

'''




