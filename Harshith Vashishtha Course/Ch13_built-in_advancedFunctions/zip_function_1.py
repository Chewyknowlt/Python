#zip 2 lists-> each element of same index zip together in tuple which  is inside  of list
user_id = ['user1' , 'user2', 'user3']
names = ['hamza', 'uzair', 'khurram']
print(list(zip(user_id, names)))

# if any list has less element as compared-> zip won't for remainig element
user_id = ['user1' , 'user2', ] # 1 less element, thus it zip upto 2 elements 
names = ['hamza', 'uzair', 'khurram']
print(tuple(zip(user_id, names)))

#More lists can be zipped alongside
user_id = ['user1' , 'user2', 'user3']
names = ['hamza', 'uzair', 'khurram']
last = ['arain', 'qureshi', 'khan']
print(list(zip(user_id, names, last)))