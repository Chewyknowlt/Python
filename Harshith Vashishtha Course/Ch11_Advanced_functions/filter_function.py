lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#filter() -separate only true cond.

is_even = list( filter(lambda n : n%2 == 0, lst) ) # filter() 
print(is_even) #this return only true value

is_even = list( map(lambda n : n%2 == 0, lst) )  #map()
print(is_even) # this return both true and false

# filter() & map() both are iterator but not called 2nd time
a =  filter(lambda n : n%2 == 0, lst)  #  map(lambda n : n%2 == 0, lst)
for i in a:
     print(a)  # 1st time -> workable
for i in a : print(a) #2nd time -> Not working

#By list Comprehension
m = [i for i in lst if i%2 == 0]
print(m)