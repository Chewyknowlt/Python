# set Comprehension

# set of 1-100
s = {i for i in range(1, 11)}
print(s)

#set 1st char of each name
names = ['Hamza', 'Wajiha', 'Mahnoor']
char1 = {name[0] for name in names}
print(char1)