from collections import OrderdDict

favourite_languages = OrderdDict()

favourite_languages['hamza'] = 'Python'
favourite_languages['Amaan'] = 'C#'
favourite_languages['Zia'] = 'Java'
favourite_languages['kumail'] = '.Net Core'

for name, language in favourite_languages.items():
    print(name.titile() + ' \'s favourite language is ' +
          language.title() + '.')
