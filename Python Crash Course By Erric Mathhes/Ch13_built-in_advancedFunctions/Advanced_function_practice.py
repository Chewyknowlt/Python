# f() -> pass n no. of lists as arg & return average of same index value
# e.g; [1, 2, 3] [4, 5, 6] --> (1+4)/2   (2+5)/2  (3+6)/2

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8 ,9]

#Simple way
def avg_find(*args): #Take n no. of parameters -> ( [ ], [ ] )
    empty = []
    for pair in zip(*args): # this args unpack tuple -> [ ], [ ]
        empty.append(sum(pair)/len(pair))
    return empty

print(avg_find(l1, l2, l3))

#extreme compact way
avg  = lambda *args : list(sum(pair)/len(pair) for pair in zip(*args))
print(avg(l1, l2, l3))