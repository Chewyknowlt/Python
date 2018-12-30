print('6-7. People\n')

peoples = []

people = {
    'first_name':'Muhammad Hamza',
     'last_name':'Hanif',
           'age': 21,
          'city': 'Karachi'
        }
peoples.append(people)

people = {
    'first_name':'Uzair',
     'last_name':'Qureshi',
           'age': 20,
          'city': 'Karachi'
        }
peoples.append(people)

people = {
    'first_name':'Khurram',
     'last_name':'Khan',
           'age': 19,
          'city': 'Karachi'
        }
peoples.append(people)

# Maiking list wcich involve dictionary.
for people in peoples:
    name = people['first_name'] + ' '+ people['last_name']
    age = str(people['age'])
    city = people['city']

    print('name: ', name, '\nAge:  ', age, '\nCity: ', city,'.\n')
