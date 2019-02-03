print('8-13. User Profile')

def build_user(first, last, ** user):
    # ** <parameter> describe dictionary.
    profile = {}
    profile['first_name'] = first
    profile['last_name']  = last
    for key, value in user.items():
        profile[key] = value.title()
    return profile

user_profile = build_user('hamza', 'hanif',
                          location = 'karachi',
                          field = 'CS')
print(user_profile)
 
