#else, finally 

while True:
    try:
        age = int(input("Enter age: "))
    except ValueError: #if try-> error of ValueError -> this work
        print('Enter int') 
    except: #if not ValueError -> this work
        print('Unexpected error')
    else: #if  try ->no error, else -> work
        print(f"Age : {age}") 
        break
    finally: #thid always work
        print('Finally')
