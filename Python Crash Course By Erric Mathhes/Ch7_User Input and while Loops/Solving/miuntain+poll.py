responses = {}
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input('What\'s your name?')
    response = input('Which mountain would you like to climb somday?')

    # Store response indictionary.
    responses[name] = response

    # Find out of anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the result.
print('\n---Poll Redut---')

for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')
print(responses)
