print('9-1. Restaurant')

#Class which takes two instances.
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('I love this ' + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open')

#Applying.              
my_favorite_retaurant = Restaurant('Taj', 'custered')
print('\nMy favorite restaurant is ' +
      my_favorite_retaurant.restaurant_name.title() + ' & I\'d love to eat '+
      my_favorite_retaurant.cuisine_type.title() + '.')

your_favorite_restaurant = Restaurant('Pearl Continental', 'muffin')
print('Your favorite restaurant is ' +
      your_favorite_restaurant.restaurant_name.title() +  ' & you\'d love to eat '+
      your_favorite_restaurant.cuisine_type.title() + '.')
