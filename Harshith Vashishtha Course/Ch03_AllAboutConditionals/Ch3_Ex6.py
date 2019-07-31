# guessing game
import random
counter = 0
winning_number = random.randint(1, 100)
while(True):
    guess = int(input("Enter number: ")) 
    counter += 1
    if (guess == winning_number):
        print(f"After {counter} times, you won")
        break

    elif (guess >= winning_number) : print(f"{guess} is greater")
    else : print(f"{guess} is lower")
