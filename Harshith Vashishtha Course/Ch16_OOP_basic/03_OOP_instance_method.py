# Person class
class Person:
    # Creating constructor
    def __init__(self, f_name, l_name, age):
        #Creating instance/obj
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.age = age

        self.full_name = f_name.title() + ' ' +l_name.title() #creating instance out of attribute

    #display full_name
    def display_name(self):
        return f"{self.full_name}"

    #return age is over 18 in Ture/False
    def above_18(self):
        return self.age > 18

# Creating obj/instance
p1 = Person('hamza', 'arain', 22)
p2 = Person('uzair', 'qureshi', 20)

# Calling class
print(p1.above_18())            #Method 1
print(Person.above_18(p2)) #Method 2