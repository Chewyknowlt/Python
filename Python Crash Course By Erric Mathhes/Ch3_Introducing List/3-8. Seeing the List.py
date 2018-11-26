print('3-9. Seeing the World')

#sorted in alphabetical order.
locations = ['UK','SDA','ENG','CHI','GER']
loc = sorted(locations)
print('sorted(): ')
print(loc)
print('Orginal: ')
print(locations)

#sorted in reverse order.
loc.sort(reverse = True)
print('sort() in reverse: ')
print(loc)
print('Original: ')
print(locations)

# reverse()
locations.reverse()
print(locations)

# again reverse
locations.reverse()
print(locations)

# sort()
locations.sort()
print(locations)

#sort() in reverse()
locations.reverse()
locations.sort()
print(locations)

