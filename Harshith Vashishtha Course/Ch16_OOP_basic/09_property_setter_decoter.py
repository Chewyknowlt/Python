class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0) #_price ->indicating private instance, if usr pass -ve it convert into 0.
        # self.specification = self.brand + ' ' +self.model + ', Rs: ' + str(self._price) 
        #specificatin cant update after manking obj cause when obj created,
        #  __init__ already maintained. to overcome we create method

    #making method as property
    @property #we can call this method as attribute
    def specification(self): 
        return self.brand + ' ' +self.model + ', Rs: ' + str(self._price) 
    
    #restricted to update only valid no. -> gether()&setter()
    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, new_price):
        self.price = max(new_price, 0)

p1 = Phone('Nokia', '1100', 3000)
p1._price = 5000  # this will send to @property deco. instead of sending constructor as it is immutable
print(p1.price)
print(p1.specification) #property