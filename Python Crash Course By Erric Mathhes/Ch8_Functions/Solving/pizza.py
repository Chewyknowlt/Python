'''
def make_pizza(size, * toppings):
    #  Mixing positional & arbitrary arguments.
    print('\nThe following size: ' + str(size) + '"')
    for topping in toppings:
        print('-' + topping)
        
import pizza
pizza.make_pizza(15,'mushrooms')
'''

def make_pizza(size, *toppings):
    #Summarize the pizza we are about to make.
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

#from pizza import make_pizza as mp 


