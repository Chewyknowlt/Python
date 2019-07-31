# guessing number
gussed_number = int(input("Enter number: "))
winning_number = 8
if gussed_number == winning_number :  print("You have won it!")
else:
    if gussed_number >= winning_number : print("The number is greater.")
    else : print("The number is lower.")