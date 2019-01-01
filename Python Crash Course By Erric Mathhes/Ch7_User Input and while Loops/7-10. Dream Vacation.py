print('7-10. Dream Vacation')

#prompt for input
name_prompt = 'What\'s your name: '
visit_prompt = 'A place where you want to go: '
debug_prompt = 'Do you want to submit your pont again? (y/n)'

response = {}

while True:
     name = input(name_prompt)
     visit = input(visit_prompt)

     #Putting in ductionary.
     response[name] = visit

     # Maiking cndition to break.
     if input(debug_prompt) == 'n':
         break

# To show items in dictionary,
for name, place in response.items():
    print(name + ' will visit ' + place + '.')
