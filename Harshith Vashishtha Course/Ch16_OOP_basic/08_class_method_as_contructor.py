class Person:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.age = age

    #creating static method -> doesnt belong to class&obj
    @staticmethod
    def this_static_method():
        return 'This is static method.'

    def display_name(self):
        return f"{self.f_name + ' ' + self.l_name}"

# Calling class constructor
print(Person.this_static_method())