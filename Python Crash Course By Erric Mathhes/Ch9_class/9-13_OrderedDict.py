print('9-13. OrderdDict Rewrite')

from collections import OrderedDict

glossary = OrderedDict()
glossary['tuple'] = 'can\'nt change.'
glossary['list'] = 'this can be change.'
glossary['function'] = 'it is simple way to handle situations.'

for term, definition in glossary.items():
    print(term.title() + ': ' + definition.capitalize())
