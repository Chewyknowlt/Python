print('5-11. Ordinal Numbers')

# Cardinal numbers.
cardinal_numbers = [1,2,3,4,5,6,7,8,9]

# Making cond. cardinal to ordinal numbers.
for cardinal_number in cardinal_numbers:
    if cardinal_number == 1:
        print(str(cardinal_number) + 'st' )
    elif cardinal_number == 3:
        print(str(cardinal_number) + 'rd')
    else:
        print(str(cardinal_number) + 'th')
