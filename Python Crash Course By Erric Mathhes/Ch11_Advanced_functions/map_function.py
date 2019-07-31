nums= [1, 2, 3]
def sqr(n) : return n**2

#map([ lambda/function ], [ list/tuple ])
sqr_list = list(map(sqr, nums)) # 1.    sqr() as arg 
print(sqr_list) #list

sqr_list = tuple(map(lambda n : n**2, nums)) #2.    lambda as arg
print(sqr_list) #tuple

q = map(lambda n : n**2, nums) #2.   making q as object of map()
for i in q : print(i) #1st time is iterable

for i in q: # 2nd time will not work 
    print(i, 'this will not work')

# 3.    list Comprehension
s = [i ** 2 for i in nums]
print(s)