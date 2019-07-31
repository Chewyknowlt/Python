#laptop class
class Laptop:
    # creating contructor   
    def __init__(self, brand, model, price):
        #define more instances than attributes
        self.brand = brand 
        self.model = model 
        self. price = price  
        self.brand_name = brand + ' ' + model #xtra instance  than sttributes

# creating 2 objs
lap1 = Laptop('hp', 'ebook-elite', 30)
lap2 = Laptop('Apple', 'Notebook', 250000)

# Calling objs 
print(lap1.brand_name)