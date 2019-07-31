# Ask user for input name & reverse it
# make it 2 line using string formatting

name = input("Enter name: ")  #Prompt user for input
print(f"Reversed Name: {name[ : :-1]}") # formatted name

#2nd way in 1 line
print(input("Enter your name: ") [::-1])