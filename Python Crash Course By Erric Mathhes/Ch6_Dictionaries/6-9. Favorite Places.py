print('6-9. Favorite Places')

favorite_places = {
    'hamza'   : ['london','paris', 'new york'],
    'wajiha'  : ['kashmir','vance','paris'],
    'mahnoor' : ['gilgit', 'saif ul muluk', 'islamabad']
    }

# Looping of dictionary through nestig. 
for name, places in favorite_places.items():
    print('\n' + name.title() + ' like these places:')
    #list inside dictionary.
    for place in places:
        print(place.title())
    
