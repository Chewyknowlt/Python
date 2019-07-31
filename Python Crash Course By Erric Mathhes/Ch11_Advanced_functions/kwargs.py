# kwargs as parameter
def dic(**kwargs):  
    for k, v in kwargs.items():  
        print(f"{k} : {v}")

#Passing argument 
print(dic(first = "Hamza", last = "Arain"))

#kwargs as argument
d = {'name' : 'Hamza', 'age' : 22}
print(dic(**d)) #unpacking dictionary -> d**