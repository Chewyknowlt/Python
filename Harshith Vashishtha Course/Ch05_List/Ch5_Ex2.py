# Reverse list using pop() & append()

def reverse_list(list): #Limtized version
    reversed = []
    while len(list) != 0:
        popped_item = list.pop()
        reversed.append(popped_item)
    return reversed

def smart_reverse_list(list): # My version
    return list[::-1]  #or list[-1::-1] or list.reverse()

numbers = [1,2,3,4] 
print(reverse_list(numbers)) #Limtized version

numbers =   list(range(1,5)) #generating list upto 4
print(smart_reverse_list(numbers)) # My version