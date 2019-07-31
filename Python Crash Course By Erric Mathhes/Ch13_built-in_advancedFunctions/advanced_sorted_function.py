# sorted( [lst/dict], key =  [function], revers = [True/False])

guitars = [
    {'model' : 'yammaha 1', 'price' : 8400},
    {'model' : 'yammaha 2', 'price' : 5000},
    {'model' : 'yammaha 3', 'price' : 35000},
    {'model' : 'yammaha 4', 'price' : 45000}
]

low_high = sorted(guitars, key = lambda dic : dic['price'])
print(low_high) #low to high order

high_low = sorted(guitars, key = lambda dic : dic['price'], reverse = True)
print(high_low) #Reverse order