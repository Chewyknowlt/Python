# Method 1
def is_even(list):
    return  [True if n%2 == 0 else False for n in list]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(is_even(lst))

# Using lambda expressions
even = lambda list : [True if n%2 == 0 else False for n in list]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even(lst))