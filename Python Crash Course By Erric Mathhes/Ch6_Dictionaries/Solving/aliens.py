'''
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

# Nesting dictionaries in list.
aliens = [alien_0, alien_1, alien_2]

# making loop of nested list-dictionary.
for alien in aliens:
    print(alien)
'''

# Make an empty list for storing aliens.
aliens = []
# Make 30 Aliens.
for alien in range(30):
    new_alien = {'speed' : 'slow', 'color' : 'green', 'points' : 5}
    aliens.append(new_alien)

#Modification of first 3.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# show first 5.
for alien in aliens[:5]:
    print(alien)
print('............')

# how many have been generated.
print('Total: ' + str(len(aliens)))
