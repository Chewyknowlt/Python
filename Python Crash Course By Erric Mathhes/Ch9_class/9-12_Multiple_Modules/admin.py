from user import User

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name ,last_name, username, email)
        self.allow_admin = Privileges()
    
class Privileges():
    def __init__(self, privileges = []):
        self.allow_privileges = privileges

    def show_privileges(self):
        # Making Loop.
        for privilege in self.allow_privileges:
            print('Only Admin can do this ' + '"' +
                  privilege.title() + '"' + '.')








            
