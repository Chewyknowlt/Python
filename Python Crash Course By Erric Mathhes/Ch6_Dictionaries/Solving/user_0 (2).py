# making dictionary.
favorite_languages = {
    'Hamza'   : 'python',
    'Asma' : 'c',
    'Shiza'  : 'ruby',
    'Saad'    : 'python'
    }

# Making loops in dictionary.

#items() method, approach both keys & values.
for name, language  in favorite_languages.items():
    print(name.title() + language.title())
print()
    
# sorted() to make it alphabetical order.
# keys() method, approach to keys.
for name  in sorted(favorite_languages.keys()):
    print(name.title() + ' thanks')
print()
    
# set() used not to repeat values or key.
# values() method to approach values.
for language in set(favorite_languages.keys()):
    print(language.title() + ' I like it.')
