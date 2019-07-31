class Phone: 
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = price 

    def display_info(self):
        return self.brand + ' ' +self.model

     #when we call obj ot by default this returned if __str__ not there reper call it self
    def __repr__(self): #this is for to create obj
        return (f' \'{self.brand}\' \'{self.model}\' \'{self._price}\' ')

    #when we call obj ot by default this returned  firstly
    def __str__(self):  #nicely foramtted str
        return (f' {self.brand} {self.model} {self._price} ')

    def __len__(self):  #len of strig resides in function
        return len(self.display_info())  #method calling inside method ->self.<method>
    
    def __add__(self, other): #this add two int belogs to diff objs
        return self._price +other._price
 
p = Phone('Nokia', '1100', 3000)
p1 = Phone('Sony', 'Xperia', 10000)
print(p)       #this will call str without calling str
print(repr(p))  #this will call repr
print(len(p))
p          rint(p + p1)