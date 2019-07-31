class Phone: #parent class/base class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return self.brand + ' ' +self.model

class SmartPhone(Phone): # child class/derived class
    def __init__(self, brand, model, ram):  #2 ways of inheritance
        # Phone.__init__(self, brand, model, price) #uncommon
        super().__init__(brand, model) #common 
        self.ram = ram
        
class Flagship(SmartPhone):
    def __init__(self, brand, model, ram, camera):
        super().__init__(brand, model, ram)
        self.camera = camera

    def display_info(self): # method overriding with parent class
        return self.ram + ' ' + self.brand + ' ' + self.camera

oppo_a3s = Flagship('Oppo', 'A3s', '2 GB', '11 mega pixel camera')
print(oppo_a3s.display_info()) #returns Flagship's method
print(help(oppo_a3s)) #chech Mro, multi order resolution
print(isinstance(oppo_a3s, Flagship))    #check is obj blongs to given class -> T/F
print(issubclass(SmartPhone, Phone))   #check chiled class  blongs to given parent class -> T/F