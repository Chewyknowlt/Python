even_true = [2 ,4 ,6 ,8 , 10]
even_false = [2 ,4 ,5 ,8 , 10] # false ->5
even_any = [1, 3, 5, 7, 20] # true -> 20

#all()  - Ant false in list it returns false
# [True, True, False] ---> False
# [True, True, True]---> True 

print( all([n%2 == 0 for n in even_true]) )  #even_true -> True
print( all([n%2 == 0 for n in even_false]) )  #even_false -> False

#any() - Any true return true
# [True, False False] ---> True
print( any([n%2 == 0 for n in even_any]) )  #even_any -> True