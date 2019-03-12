print('9-7 Admin')

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

    def greet_user(self):
        #Greet user.
        print(self.first_name + '! Welcome back.')

    def increment_login_attempts(self):
        #Adding no. of attempts by 1.
        self.login_attempts += 1

    def reset_login_attempts(self):
        #reset no. of attempts.
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name ,last_name, username, email)
        self.privileges = []

    def show_privileges(self):
        
        # Making Loop.
        for privilege in self.privileges:
            print('Only Admin can do this ' + '"' +
                  privilege.title() + '"' + '.')
    

ad_min = Admin('muhammad hamza','hanif',
            'Hamza.arain18',
            'hamzaarain1999@gmail.com')
ad_min.describe_user()

ad_min.privileges = ['You can delete posts',
              'You can delete account your account.',
              'You have privileges to attempts some tasks.']
ad_min.show_privileges()
