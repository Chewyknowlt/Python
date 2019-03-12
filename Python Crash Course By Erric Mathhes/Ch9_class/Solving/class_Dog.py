# makibg class of name & age.
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now siting.')

    def roll_over(self):
        print(self.name.title() +' is now roll over ' +
              ' whose age is ' + str(self.age) + '.')


my_dog = Dog('hira', 6)
your_dog = Dog('lucy', 4)
print(my_dog.name.title() + ' is my favourite whose age is ' +
      str(my_dog.age))

my_dog.sit()
my_dog.roll_over()

print(your_dog.name.title() + ' is my favourite whose age is ' +
      str(your_dog.age))

your_dog.sit()
your_dog.roll_over()
