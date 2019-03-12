print('9-3. Users:')

#class for university student.
class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def oath(self):
        print('I ' + self.first_name.title() + ' ' + self.last_name.title() +
              ' won\'t involve in political activities.')

    def dcs(self):
        print(self.first_name.title() + ' is a student of CS.')

    def section(self):
        print(self.first_name.title() + ' is a student of section A.')

#Applying.
student = User('muhammad hamza', 'hanif')
print('Student\'s full name: ' + student.first_name.title() + ' ' +
      student.last_name.title())
student.oath()
student.dcs()
student.section()
