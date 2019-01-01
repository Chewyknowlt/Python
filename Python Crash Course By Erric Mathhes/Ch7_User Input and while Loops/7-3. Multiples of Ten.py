print('7-3. Multiples of Ten')

ask = int(input('Is the number is multiple of 10 or not?'))
if ask % 10 == 0:
    print(str(ask) + ' is divisible by 10.')
else:
    print(str(ask) + ' is not divisible by 10.')
