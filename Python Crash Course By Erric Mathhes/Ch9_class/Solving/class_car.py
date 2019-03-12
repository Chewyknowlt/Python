'''
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

#Applying.
my_old_car = Car('Suzuki', 'corrola',2019)
print(my_old_car.get_descriptive_name())

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

'''

'''
#Implementing default value.
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

#Applying.
my_old_car = Car('Suzuki', 'corrola',2019)
print(my_old_car.get_descriptive_name())
my_old_car.read_odometre()
'''

'''
#Modifying attributes directly.
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

my_old_car = Car('Suzuki', 'corrola',2019)
print(my_old_car.get_descriptive_name())
my_old_car.odometre_reading = 23 #Modifying attribute's value directky.
my_old_car.read_odometre() #Calling it.
'''

'''
#Modifying attribute's value through method.
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

    def update_odometre(self, mileage): #MOdifying.
        #Modifying value.
        self.odometre_reading = mileage
        
my_old_car = Car('Suzuki', 'corrola',2019)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometre(25)
my_old_car.read_odometre()
'''

'''
#Modifying attribute's value through method with little logic that no one roll back.
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

    def update_odometre(self, mileage): #MOdifying.
        # milage >= older milagge tht no one roll back.
        if milage >= self.odometre_reading:
            self.odometre_reading = mileage
        else:
            print('You can\'t roll back!')
            
my_old_car = Car('Suzuki', 'corrola',2019)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometre(25)
my_old_car.read_odometre()
'''

'''
#Modifying increments through method.
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

    def update_odometre(self, mileage): #MOdifying.
        #milage >= older milagge tht no one roll back.
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage # for older mileage to add some more.
        else:
            print('You can\'t roll back!')

    def increment_odometre(self, miles):
        # it is for old car which has some  milage >= older milagge. 
        self.odometre_reading += miles   

my_old_car = Car('Suzuki', 'corrola',2019)
print(my_old_car.get_descriptive_name())

my_old_car.update_odometre(24355)
my_old_car.read_odometre()

my_old_car.increment_odometre(100)
my_old_car.read_odometre()
'''

'''
#Making child class under super class.
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

    def update_odometre(self, mileage): #MOdifying.
        #milage >= older milagge tht no one roll back.
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage # for older mileage to add some more.
        else:
            print('You can\'t roll back!')

    def increment_odometre(self, miles):
        # it is for old car which has some  milage >= older milagge. 
        self.odometre_reading += miles   

#making child class.
class Electric_Car(Car):
    #represent as respect to elec. car.

    def __init__(self, make, model, year):
        #init. attrubutes of main class.
        super().__init__(make, model, year)

my_tesla = Electric_Car('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
'''

'''
#Making child class under super class + adding method to it.
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

    def update_odometre(self, mileage): #MOdifying.
        #milage >= older milagge tht no one roll back.
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage # for older mileage to add some more.
        else:
            print('You can\'t roll back!')

    def increment_odometre(self, miles):
        # it is for old car which has some  milage >= older milagge. 
        self.odometre_reading += miles   

#making child class.
class Electric_Car(Car):
    #represent as respect to elec. car.

    def __init__(self, make, model, year):
        #init. attrubutes of main class.
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('Battery size: ' + str(self.battery_size) + '-KWH')

my_tesla = Electric_Car('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
'''

'''
#Overriding method fill_gas_tank().
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.' )

    def fill_gas_tank(self):
        print('Car has ability of fuelling he tank.')

    def update_odometre(self, mileage): #MOdifying.
        #milage >= older milagge tht no one roll back.
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage # for older mileage to add some more.
        else:
            print('You can\'t roll back!')

    def increment_odometre(self, miles):
        # it is for old car which has some  milage >= older milagge. 
        self.odometre_reading += miles   

#making child class.
class Electric_Car(Car):
    #represent as respect to elec. car.

    def __init__(self, make, model, year):
        #init. attrubutes of main class.
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('Battery size: ' + str(self.battery_size) + '-KWH')

    def fill_gas_tank(self):
        print('Car has no callable of fuelling tank.')

my_tesla = Electric_Car('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
'''

'''
#Attributes as instances.
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.')

    def fill_gas_tank(self):
        print('Car has ability of fuelling he tank.')

    def update_odometre(self, mileage): #MOdifying.
        #milage >= older milagge tht no one roll back.
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage # for older mileage to add some more.
        else:
            print('You can\'t roll back!')

    def increment_odometre(self, miles):
        # it is for old car which has some  milage >= older milagge. 
        self.odometre_reading += miles   

class Battery():
    #A simple attemot to model a battery.
    
    def __init__(self, battery = 70):
        #init battery attri.
        self.battery = battery

    def describe_battery(self):
        #Descrobe battery.
        print('Battery size: ' + str(self.battery) + '-KWH')

#making child class.
class Electric_Car(Car):
    #represent as respect to elec. car.

    def __init__(self, make, model, year):
        #init. attrubutes of main class.
        super().__init__(make, model, year)
        self.battery = Battery()
    
#applying.
my_tesla = Electric_Car('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
'''

#.
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0 # making default value.
        
    def get_descriptive_name(self):
        #return neatly descriptve name.
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        #Showing speed of car.
        print('This car\'s milage ' + str(self.odometre_reading) + '.')

    def fill_gas_tank(self):
        print('Car has ability of fuelling he tank.')

    def update_odometre(self, mileage): #MOdifying.
        #milage >= older milagge tht no one roll back.
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage # for older mileage to add some more.
        else:
            print('You can\'t roll back!')

    def increment_odometre(self, miles):
        # it is for old car which has some  milage >= older milagge. 
        self.odometre_reading += miles   

class Battery():
    #A simple attempt to model a battery.
    
    def __init__(self, battery = 70):
        #init battery attri.
        self.battery = battery

    def describe_battery(self):
        #Descrobe battery.
        print('Battery size: ' + str(self.battery) + '-KWH')

    def get_range(self):
        #range of battery.
        if self.battery == 70:
            range = 240
        elif self.battery == 85:
            range = 270
        message =('This car can go approx. ' + str(range))
        message += (' miles on a full charge.')
        print(message)
        
#making child class.
class Electric_Car(Car):
    #represent as respect to elec. car.

    def __init__(self, make, model, year):
        #init. attrubutes of main class.
        super().__init__(make, model, year)
        self.battery = Battery()
    
-#applying.
my_tesla = Electric_Car('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()

        

