#Make custom error
class NameLengthShort(ValueError): #inherit ValueError cls
    pass

def name_len_prompt(name):
    if len(name) <= 8:
        raise NameLengthShort("Name is too short")

username = input('Enter name: ')
name_len_prompt(username)
print('Hello!' + username.title())