# make func that contain every data 
# and separate out only int and float 
# convert it into string
def int_float_separator(list):
    return [str(num) for num in list if type(num) == float or type(num) == int]

lst = [1, 0.1, "C", 's' ,[] ,{}, True, False, None,    [1, 0.1, "C", 's', [], {}],     {1: [], 2: {}} ]
print(int_float_separator(lst))