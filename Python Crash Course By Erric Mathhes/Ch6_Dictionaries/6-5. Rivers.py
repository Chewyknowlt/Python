print('6-5. Rivers')

rivers = {
    'nile'  : 'egypt',
    'swiss' : 'newzealand',
    'indus' : 'pakisatan'
    }

# Loop in dictionary.
for river, country in rivers.items():
    print('The ' + river.title() + ' river is run by ' +
          country.title() + '.')
