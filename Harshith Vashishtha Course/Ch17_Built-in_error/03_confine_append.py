class Mobile:
    def __init__(self, name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New mobile should be obj of mobile class')

oppo = Mobile('one plus 6') #obj of cls Mobile
samsung = 'Samsung Galaxy S8'  # out of cls Mobile
store = MobileStore()  #making MobileStore cls
store.add_mobile(oppo) #append mobile cls obj
mobile_phones = store.mobiles # list obj
print(mobile_phones[0].name) # show appended list
# store.add_mobile(samsung)  #this throws error