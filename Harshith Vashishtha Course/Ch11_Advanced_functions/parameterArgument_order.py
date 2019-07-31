#Passing all parametre within order
#PADK
#Parametre
#args
# Defalut
# Kwargs

def parameter_order(name, *args, age = None , **kwargs):
    print(f'Normal parameter : name : {name}')
    print(f'*args parameter : *args : {args}')
    print(f'Default parameter :  age : {age}')
    print(f'**kwargs parameter : **kwargs : {kwargs}')

#parameter values
name = "Hamza" #Normal argument
lst = ['1',' 2', '3']        # or tupl = (1, 2, 3) -> *args argument
age = 22   #  it's default parameter
d = {'1' : 'Python',  '2': 'C#', '3': 'JAVA Script'}   # As **kwargs argument 

#Calling these all
parameter_order(name, age = 22,*lst,  **d)


 