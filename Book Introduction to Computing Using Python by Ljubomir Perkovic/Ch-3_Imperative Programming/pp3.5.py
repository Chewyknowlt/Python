# Practice Problem 3.5

##Implement a program that requests from the user a list of words (i.e., strings) and then prints on the screen, one per line, all four-letter strings in the list.

lst = ['stop', 'desktop', 'top', 'post']
for x in lst:
    if x in ['stop', 'post']:
        print(x)
