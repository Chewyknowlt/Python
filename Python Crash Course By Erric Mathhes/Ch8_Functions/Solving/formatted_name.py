'''
def get_formatted_name(first_name, middle_name, last_name):
    #Return a full name, neatly formatted.
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

# Calling fuction from variable.
player = get_formatted_name('shaihid', 'khan' ,'afridi')
print(player)
'''

'''
def get_formatted_name(first_name, last_name, middle_name=''):
    #Return a full name, neatly formatted.
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# Makuing optional argument.
player = get_formatted_name('shaihid', 'khan')
print(player)

player = get_formatted_name('shaihid', 'khan','afridi')
print(player)
'''

'''
def get_formatted_name(first_name, middle_name, last_name):
    #Return a full name, neatly formatted.
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

#This is an infinite loop!
while True:
    print('\nPlease tell me your name: ')
    f_name = input('First Name: ')
    m_name = input('Middle Name: ')
    l_name = input('Last Name: ')

    formatted_name = get_formatted_name(f_name, m_name, l_name)
    print('\nHello, ' + formatted_name + '!')
'''

def get_formatted_name(first_name, last_name):
    #
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\n Please tell me your name: ')
    print('(Enter \'q\' anytime to quit)')

    f_name = input('First Name: ')
    if f_name == 'q':
        break

    l_name = input('Last Name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')














