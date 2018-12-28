print('5-5. Alien colors #3')

# Using if-elif-else statements.
alien_color = ['green','red','yellow']
for color in alien_color:
    if color == 'green':
        points = 5
    elif color == 'yellow':
        pointss = 10
    else:
        points = 15
    print('You\'ve got ', points, ' points to shot down alien of color' ,color,'.')
        
