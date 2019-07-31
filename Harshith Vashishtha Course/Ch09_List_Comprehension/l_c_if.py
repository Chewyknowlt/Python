# Separating even and odd
numbers = list(range(1, 11))
even_nums = [i for i in numbers if i%2 == 0] # even
odd_nums = [i for i in numbers if i%2 != 0] # odd

print(even_nums)
print(odd_nums)