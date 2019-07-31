#laptop class
class Laptop:
    # creating contructor   
    def __init__(self, brand, model, price):
        #define more instances than attributes
        self.brand = brand 
        self.model = model 
        self. price = price  
        self.brand_name = brand + ' ' + model #xtra instance  than sttributes

    #This returns discount
    def apply_discount(self, percentage):
        discount =  percentage*self.price/100
        return self.price - discount

# creating 2 objs
lap1 = Laptop('hp', 'ebook-elite', 30000)
lap2 = Laptop('Apple', 'Notebook', 250000)

# Calling objs 
print(lap1.apply_discount(50))