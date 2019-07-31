#Ask user to 3 inputs separated by commas 
#make it there average 
#print formatted output 

#a=[eval(b) for b in input().split(',')] 
#print( f"{sum(a)/len(a)}" )

num1, num2, num3 =input("Enter # three time separated by ','  : ").split(',')  #multiple inputs splited by comma
print(f"Average: { ((float(num1) + float(num3) + float(num3))/3) }") # py 3.6 formatted