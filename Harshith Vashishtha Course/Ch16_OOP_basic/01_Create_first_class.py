# Creating 1st class

#Creating class of Person
class Person: 
    def __init__(self, f_name,):  
        # def __init__ or constructor
        # self = obj name, by default it comes first instead self it can be used anyth in
        #After self, other are attribiutes of class e,g; f_name, l_name
        
        self.f_name = f_name # this is also called instance

# creating obj
p1 = Person('hamza')
p2 = Person('Saad')

#calling objs
print(p1.f_name) 
print(p2.f_name)