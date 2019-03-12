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
    
