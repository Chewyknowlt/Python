print('6-4. Glossary 2')

glossary = {
    'string'    : 'A series of characters.',
    'comment'   : 'A note in a program that the Python interpreter ignores.',
    'list'      : 'A collection of items in a particular order.',
    'loop'      : 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple'     : 'It \'s immutable.',
    'nesting'   : 'Loop under loop.',
    'if-if'     : 'it read all conddition.',
    'else'      : 'It will cath all remaing condition that is false.',
    'if-elif'   : 'it reads untill only true condition occur.'
    }

# Making dictionary loop.
for k, v in glossary.items():
    print('\n' + k + ' : ' + v)
