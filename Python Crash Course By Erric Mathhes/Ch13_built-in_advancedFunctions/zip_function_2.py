#uses of zip()
# 1.  --> l1 = [1, 3, 5, 7, 9], l2 = [2, 4, 6, 8, 10]
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#print(list( zip(*lst) ))
l1, l2 =  zip(*lst) # devide each each element with corresponding index
print(l1) # tuple
print( list(l2) )  #list

# 2. Comparing values simultaneously with index correspondingly 
lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 10] 
# m = list( map( max , zip(l1,l2) ) )
m = []
for pair in zip(l1,l2): #m = list( map( lambda pair : max(pair), zip(l1,l2) ) )
    new.append(pair)
print(m) 

# 3. Using elements of iterable simultaneously
maximum = [i + j for i, j in zip(l1, l2)]
print(maximum)