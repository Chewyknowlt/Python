print('5-8. Hello Admin')

# Making loop & using if-else chain.
login = input(str('Enter name: '))
usernames = ['admin','hamza','urmila','meher','unzila']
for username in usernames:
    if username == login:
        print('Hello!' + str(username) +' you\'re in.')
        if  username == 'admin':
            print('Do you like to see the ststus?.')
    else:
        print(username + ' You\'re not in.')
