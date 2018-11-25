print("Prablem 3.33")

s = input("Enter word of 3 letters: ")
def reverse(s):
    if len(s) == 0:
        return s 
    else:
        return reverse(s[1:]) + s[0] 
    
print ("The original string is : ",end="") 
print (s) 

print ("The reversed string is : ",end="") 
print (reverse(s))




