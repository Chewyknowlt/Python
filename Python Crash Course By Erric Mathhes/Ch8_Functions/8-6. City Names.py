print('8-6. City Names')

#Method 1.
def city_country(city, country):
    # Printing name.
    return (print(city.title() + ', ' + country.title()))
    
city_country('karachi', 'pakistan')
city_country('washington D. C.', 'america')
city_country('london', 'england')

#Method 2.
def city_country(city, country):
    #Printing name.
    return city.title() + ', ' + country.title()

city = city_country('karachi', 'pakistan')
print(city)

city = city_country('washington D. C.', 'america')
print(city)

city = city_country('london', 'england')
print(city)

