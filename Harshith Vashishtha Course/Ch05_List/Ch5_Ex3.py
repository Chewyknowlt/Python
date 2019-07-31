# ['abc', 'tuv', 'xyz'] --> ['cba', 'vut', 'zyx']

def reverseString_inList(list):
    return [x[::-1] for x in list]

data = ['abc', 'tuv', 'xyz']
print(reverseString_inList(data))