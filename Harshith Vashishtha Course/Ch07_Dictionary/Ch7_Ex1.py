# Function takes number, and return dict.
#  contanig cube of key

def cube_dict(n):
    d = dict.fromkeys(list(range(1, n +1)), 1) # d = {}
    for i in d:                                                  # for i in range(1, n +1)
        d[i] = i ** 3                                           # as it is as below
    return d
print(cube_dict(3))