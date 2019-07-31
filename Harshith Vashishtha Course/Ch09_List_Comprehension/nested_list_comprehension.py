# example = [  [1, 2, 3],  [1, 2, 3], [1, 2, 3]  ]

# Method 1:
new_list = []
for i in range(3):
    new_list.append([1, 2, 3])
print(new_list)

#Method 2:
nested__list_comp = [  [i for i in range(1, 4)] for j in range(3)  ]
print(nested__list_comp)