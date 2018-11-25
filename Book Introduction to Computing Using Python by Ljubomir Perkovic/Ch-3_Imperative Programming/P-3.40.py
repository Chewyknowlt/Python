print('Problem 3.40')

def partition(lst):
    x = [name for name in lst
            if name[0].lower() in 'abcdefghijklm']
    print(x, end ='\n')

        
# ['Eleaenor', 'Evelyn', 'Sammy', 'Owen', 'Gavin']
