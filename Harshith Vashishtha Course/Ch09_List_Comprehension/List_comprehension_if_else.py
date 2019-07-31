# even num -> num * 2
# odd num -> - num

# Method 1
nums = list(range(1, 11))
new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i * 2)
    else:
        new_list.append(-i)
print(new_list)

# Method 2
all = [i * 2 if i%2 == 0 else -i for i in nums]
print(all)