# Making func() that reverse each element

def reverse_list(list):
    return [x[::-1] for x in lst]  # [x.reverse for x in lst]

lst = ['abc', 'tuv', 'xyz']
print(reverse_list(lst))