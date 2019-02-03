def greet_users(names):
    #greeting to each user.
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['saad', 'mona','meher']
greet_users(usernames)
