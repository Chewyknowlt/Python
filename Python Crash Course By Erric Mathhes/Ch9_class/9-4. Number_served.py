print('9-1. Restaurant')

#Class which takes two instances.
class Restaurant():

    def __init__(self, restaurant, cuisine):
        self.restaurant = restaurant
        self.cuisine = cuisine
        self.number_served = 0 # makin default value.

    def customer_deal(self): # print no. of customer.
        print('Customers dealt: ' + str(self.number_served))
        
    def update_customers(self, served): # add init customers.
        if served >= self.number_served:
            self.number_served = served
        else:
            print('You can\'t add initially.')
            
    def additional_customers(self, additional_customer): 
        # increment in old customers. 
        self.number_served += additional_customer


#Applying.              
restaurant = Restaurant('Taj', 'custerd')

restaurant.update_customers(123)
restaurant.customer_deal()

restaurant.additional_customers(100)
restaurant.customer_deal()
