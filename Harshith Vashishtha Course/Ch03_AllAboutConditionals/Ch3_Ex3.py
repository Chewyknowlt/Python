# sum of n natural numberes
# ask user to input
# sum of n natural numbers
# print total from 1 - 10

n = int(input("Enter number: "))
i = 1
total = 0
while (i <= n):
    print(f"Number: {i}")
    total += i
    i += 1
print(f"Total: {total}")