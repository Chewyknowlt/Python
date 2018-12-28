print('5-10. Checking Usernames')

# Simple list with title() case.
current_users = ['Lola','Nuru','Hola','Pappu','Munni']
new_users = ['Pappu','Myself','Selfie','Lola','Lord']

# append-loop-list for handling case sensitiveness.
current_users_lower = [current_user.lower for current_user in current_users]
new_users_lower = [new_user.lower for new_user in new_users]

#final testing to chech new user in list.
for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print('Sorry! You have to choose other names.')
    else:
        print('This name has been accepted.')

