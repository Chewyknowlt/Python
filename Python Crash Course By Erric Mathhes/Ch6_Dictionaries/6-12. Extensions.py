print('6-12. Extensions')

pet = {
    'dog'   : {
        'name'          : 'german shpfered',
        'owner'         : 'hamza'
        },
    'cat'   : {
        'name'          : 'russian blue',
        'owner'         : 'wajiha'
        },
    'horse' : {
        'name'          : 'arabian horse',
        'owner'         : 'hamza'
        }
    }

for species, species_info in pet.items():
    name = species_info['name']
    owner = species_info['owner']
    print('Specy: ' +  species.title())
    print('Name:  ' + name.title())
    print('Owner: ' + owner.title())
    print()

    
