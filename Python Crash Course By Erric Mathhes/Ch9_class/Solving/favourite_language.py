from collections import OrderedDict

favourite_language = OrderedDict()

favourite_language['hamza'] = 'pyhton'
favourite_language['amaan'] = 'c#'
favourite_language['kumail'] = 'java script'
favourite_language['zia'] = 'java'

for name, language in favourite_language.items():
    print(name.title() + '\'s favourite language is ' +
          language.title())
