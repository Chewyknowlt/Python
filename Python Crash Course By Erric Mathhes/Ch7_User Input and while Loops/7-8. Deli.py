print('7-8. Deli')

sandwich_orders = ['spicy','club','egg']
finished_sandwiches = []

while sandwich_orders:
    current_sandwitch = sandwich_orders.pop()
    print(current_sandwitch.title() + ' sandwhitch is under processing.')
    finished_sandwiches.append(current_sandwitch)

print()
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title()  + ' sandwhitch Has been ready.')
