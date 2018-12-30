print('6-11. Cities')

cities = {
    'karachi'    : {
        'country'    : 'pakistan',
        'speciality' : 'hub',
        'importance' : 'sindh capital'
        },
        
    'mumbai'     : {
        'country'    : 'india',
        'speciality' : 'hub',
        'importance' : 'maharashtra capital'
        },
        
    'vance'     : {
        'country'    : 'italy',
        'speciality' : 'beautiful',
        'importance' : 'cashing'
        }
    }

# Nesting of dictionary.
for city_name, city_info in cities.items():
    _country = city_info['country']
    _speciality = city_info['speciality']
    _importance = city_info['importance']
    print('\n' + city_name.title() +
          ' is in ' + _country.title() +
          ' whose specilaity is ' + _speciality.title() +
          ' and importance is ' + _importance + '.' )
