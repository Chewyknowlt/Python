# list compresion

#  create list of  square  from 1 - 100
sqr2 = [i ** 2 for i in range(1, 11)]
print(sqr2)

# Creating list of negative numbers from -1 - 10
negative2 = [-i for i in range(1, 11)]
print(negative2)

# Creating list of 1st char of each element from list
names = ['Kumail', 'Ayesha', 'Maham']
list_comp = [name[0] for name in names]
print(list_comp)


