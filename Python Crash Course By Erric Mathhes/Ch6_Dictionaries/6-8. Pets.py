print('6-8. Pets')

pets = []

pet = {
    'animal type'   : 'dog',
    'name'          : 'german shpfered',
    'owner'         : 'hamza'
    }
pets.append(pet)

pet = {
    'animal type'   : 'cat',
    'name'          : 'russian blue',
    'owner'         : 'wajiha'
    }
pets.append(pet)

pet = {
    'animal type'   : 'horse',
    'name'          : 'arabian horse',
    'owner'         : 'hamza'
    }
pets.append(pet)

# Making looop which nest dictionaries.
for pet in pets:
    animal_type = pet['animal type']
    name = pet['name']
    owner = pet['owner']
    print(owner  + ' own this ' + name +
          ' which belongs to ' + animal_type + '.\n')

