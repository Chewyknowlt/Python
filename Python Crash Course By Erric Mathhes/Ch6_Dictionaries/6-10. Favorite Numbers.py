print('6-10. Favorite Numbers')

dic = {
    'Uzair'   : [45, 65],
    'Hamza'   : [12, 65],
    'Khurram' : [44, 87],
    'Mohib'   : [8,9],
    'Hanif'   : [6,9]
    }

for name, numbers in dic.items():
    print('\n' + name.title() +
          ' like these numbers: ')

    for number in numbers:
        print(str(number))
