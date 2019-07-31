# as kuser for input name and count each char 

name = input("Enter: ").lower()
i = 0
temp = ""
while i < len(name):
    if (name[i] not in temp):
        temp += name[i]
        print(f"Character: {name[i]} : {name.count(name[i])}")
    i += 1
