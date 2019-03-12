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
