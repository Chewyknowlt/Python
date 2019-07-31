# ask user for input more than 1 digit
# e.g; 1234 -> 1+2+3+4 = 10

ask = input("Enter number: ")
i = total = 0
while (i < len(ask)):
    total += int(ask[i])
    i += 1
print(f"Total: {total}")