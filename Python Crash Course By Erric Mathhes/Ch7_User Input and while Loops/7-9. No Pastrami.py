print('7-9. No Pastrami')

# Empty to store data.
sandwich_orders = ['pastrami','spicy','pastrami','club','egg','pastrami']
finished_sandwiches = []

# Removing pastrami from list.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('deli has run out of pastrami.\n')

# while eliminating from last to store in variable through pop().
# append it in a list.
while sandwich_orders:
    current_sandwitch = sandwich_orders.pop()
    print(current_sandwitch.title() + ' sandwhitch is under processing.')
    finished_sandwiches.append(current_sandwitch)

# Making simple loop.
print()
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title()  + ' sandwhitch Has been ready.')

