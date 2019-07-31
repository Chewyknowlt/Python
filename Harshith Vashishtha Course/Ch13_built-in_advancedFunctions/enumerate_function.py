#def f() and return position if found else return -1 

def position_finder(list, required = None):
    if required == None : return 'No task given'
    else:
        for pos, element in enumerate(list):
            if element == required: return pos
        return -1

lst = ['abc', 'def', 'ghi']
print(position_finder(lst, 'ghi'))

