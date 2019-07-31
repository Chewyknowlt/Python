def to_power(x):
    def cal(n):
        return n**x
    return cal

# closure
cube = to_power(3)
print(cube(5))

