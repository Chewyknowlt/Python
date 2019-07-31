class Animal:
    def  __init__(self, name):
        self.name = name

    #Abstract method
    def animal_sound(self): #raise error for not defined mothod in subclass
        raise NotImplementedError('Define for each subclass')

class Dog(Animal): #it raise error as method not defined
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal): #it doesnt raise error as method defined
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def animal_sound(self): #method
        return 'mewo mewo'

doggy = Dog('Hari Lal', 'pug')
kitty = Cat('Tom', 'fish')
print(kitty.animal_sound())  # workable
print(doggy.animal_sound()) #raise error bcz method doesnt defined for subclass Dog 