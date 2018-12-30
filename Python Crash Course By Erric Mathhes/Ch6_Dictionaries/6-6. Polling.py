print('6-6. Polling')

favorite_languages = {
    'jen'   : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil'  : 'python',
    }

peoples = ['hamza','sarah','saad','phil','shiza']

# Miking loop in dictionary.
for people, language in sorted(favorite_languages.items()):
    if people in peoples:
        print(people.title() +
              '! Thanks for responding, but ypu already polled '
              + language.title() + '.')
    if people not in peoples:
        print(people.title() + ', You\'re invited to make a poll.')
        
