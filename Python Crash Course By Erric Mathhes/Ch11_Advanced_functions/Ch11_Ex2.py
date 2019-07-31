#data modeling example
def func(list, **kwargs):
    if kwargs.get('reverse_str'):  #[]get('reverse_str') == True
        return  [name[::-1].title() for name in list]
    else:
          return [name.title() for name in list]

names = ['hamza', 'arain']
print(func(names, reverse_str = True))
print(func(names))