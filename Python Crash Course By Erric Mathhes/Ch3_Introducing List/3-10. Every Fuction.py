print('3-10.Every Function')

os =['dos','windows','linux','Unix','Mac']

# Access element in list
print(os[0].title()+ ' ' + os[2].upper() + ' ' +os[-2].lower())

#using individual value from list
print("Most powerful is" + ' ' + os[-3] + ".")

#changing in list.
os[0] = 'Debian' 
print(os)

#adding in list.
os.insert(0,'MINT')
print("The Addition is" + ' :')
print(os)

#Removing item in the list
os.remove('Unix')          # Permanent
print("The removal is"+ " :")
print(os)
os.pop(-1)                 # Temporary
print("The pop is" + " :")
print(os)

# Organizing List

# Permanent
os.sort()                  # Alphabetical order 
print('In alphabetical order(PER)' + ' :')
print(os)

os.sort(reverse = True)    # Reverse order
print('In reverse order(PER)' + ' :')
print(os)

#Temporary
os.sort()                  # Alphabetical order 
print('In alphabetical order(TEM)' + ' :')
print(os)

os.sort(reverse = True)    # Reverse order
print('In reverse order(TEM)' + ' :')
print(os)

# Reversing
os.reverse()
print('The reverse: ')
print(os)

#Length
print(len(os))

