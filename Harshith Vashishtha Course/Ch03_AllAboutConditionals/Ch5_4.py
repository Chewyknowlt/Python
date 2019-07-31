# filtering odd & even 

def filter_odd_even(list):
    even = []
    odd = []
    for i in list:
        if i%2 == 0: even.append(i) #even
        else:  odd.append(i)  #Odd
    filtered = [odd, even] # init. -> filtered.extend(odd)
    return filtered 

n = [1,2,3,4,5,6,7,8,9,10]
print(filter_odd_even(n))