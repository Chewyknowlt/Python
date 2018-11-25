print('Prongram 3.31')

x = float(input("Enter x cordinate: "))
y = float(input("Enter y cordinate: "))
#Predefined Data
r = 8

#Calcultaions
import math
cal = math.sqrt(x**2 + y**2)

if cal <= r:
    print("It is in!")
else:
    cal > r
    print("It is not in!")
