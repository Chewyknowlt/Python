# Practice Problem 3.4

##Implement a program that starts by asking the user to enter a login id (i.e., a string). The program then checks whether the id entered by the user is in the list ['joe', 'sue', 'hani', 'sophie'] of valid users. Depending on the outcome, an appropriate message should be printed. Regardless of the outcome, your function should print 'Done.' before terminating. Here is an example of a successful login:

name = input('Enter name: ')
user = ['joe', 'sue', 'hani', 'sophie']

if name in user:
    print('Login: ' + name)
    print('You are in!')
else:
    print('Login: ' + name)
    print('User Is unknown.')
