from Classes import Admin as C

usr =  C('muhammad hamza','hanif',
            'Hamza.arain18',
            'hamzaarain1999@gmail.com')
usr.describe_user()
print()
usr_privileges = ['You can delete posts',
              'You can delete account your account.',
              'You have privileges to attempts some tasks.']
usr.allow_admin.available_privileges = usr_privileges
usr.allow_admin.show_privileges()
