print('9-8 Privileges')
class User():
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.login_attempts = 0 # default value.

    def describe_user(self):
        #init user info.
        print('First Name : ' + self.first_name +
              '\nLast Name  : ' + self.last_name +
              '\nUser Name  : ' + self.username + 
              '\n   E-mail  : ' + self.email)

class Admin(User):
    #we're inheriting Privileges() properties in this class.
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name ,last_name, username, email)
        self.allow_admin = Privileges()
        
class Privileges():
    def __init__(self, privileges = []):
        self.available_privileges = privileges

    def show_privileges(self):
        # Making Loop.
        for privilege in self.available_privileges:
            print('Only Admin can do this ' + '"' +
                  privilege.title() + '"' + '.')
            
