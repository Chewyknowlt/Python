'''
def build_person(first_name, last_name):
    #About person from dictionary.
    person = {'first' : first_name,
              'last'  : last_name}
    return person

player = build_person('Shahid', 'Afridi')
print(player)
'''

def build_person(first_name, last_name, age = ''):
    #About person from dictionary.
    person = {'first' : first_name,
              'last'  : last_name}
    if age:
        person['age'] = age
    return person

player = build_person('Shahid', 'Afridi', age = 27)
print(player)
