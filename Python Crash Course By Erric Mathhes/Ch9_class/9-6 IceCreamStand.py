print('9-6 IceCreamStand')

#Class which takes two instances.
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0
        
    def describe_restaurant(self):
        print('I love this ' + self.restaurant_name)

    def open_restaurant(self):
        print(self.restaurant_name + ' is now open')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served
        
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type = 'Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def display_flavours(self):
        print('The Following flavours are availlable: ')
        for flavour in self.flavours:
            print(flavour.title() +' ice cream.')

faluda = IceCreamStand('pearl continental ')
faluda.flavours = ['vanilla', 'chocolate', 'stawbarry']

faluda.describe_restaurant()
faluda.display_flavours()
