# class
class Circle:
    # class variable
    pi = 3.142

    #constructor
    def __init__(self, radius):
        #instance variable
        self.radius = radius

    #instance method
    def calc_circumference(self):
        return Circle.pi * self.radius

#obj/instance
c = Circle(3)
print(c.calc_circumference())

#class
class Laptop:
    # class variable
    discount_percentage = 20
    # creating contructor   
    def __init__(self, brand, price):
        #instance variable
        self.brand = brand 
        self. price = price  

    #instance method calling 
    def apply_discount(self):
        #we you self obj instead of class variable where it is tendency of manupulation
        discount =  self.discount_percentage*self.price/100 
        return self.price - discount

#objs/instance
lap1 = Laptop('hp', 30000)

# Calling objs  
Laptop.discount_percentage = 40  #apply for every laptop obj -> class variable
print(lap1.apply_discount())
print(lap1.__dict__) # to see attributes of obj