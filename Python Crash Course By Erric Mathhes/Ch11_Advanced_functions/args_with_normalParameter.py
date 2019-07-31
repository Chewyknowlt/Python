def multiply(num, *args):
    if not args: return None # when no args given
    multiply = 1
    for n in args:
        multiply *= n
    return multiply

print(multiply(1, 2,3))   # 1st arg is positional compulsory,  2*3 = 6
                                    # 2nd and above is key argument which ia optional
print(multiply(1))         # Only positional arg has passed