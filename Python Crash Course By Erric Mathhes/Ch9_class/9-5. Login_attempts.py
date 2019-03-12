print('9-5. Login Attempt')

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
#Applying.
user = User('muhammad hamza','hanif',
            'Hamza.arain18',
            'hamzaarain1999@gmail.com')
user.describe_user()
user.greet_user()

print('\nMaking 3 login attempts: ')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print('Login attempts: ' + str(user.login_attempts))

user.reset_login_attempts()
print('Refresh login: ' + str(user.login_attempts))
