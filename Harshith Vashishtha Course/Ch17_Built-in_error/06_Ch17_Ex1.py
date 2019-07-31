divide = lambda a, b: a/b # devode function

def asking(): #ask until ans is true
    while True: #infinite loop
        try:
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            c = divide(a,b)
        except ZeroDivisionError:
            print('Denominator cant be zero')
        except ValueError:
            print('Only numbers allow')
        except:
             print('Unexpected error')
        else:
            print(c)
            break  
        finally:
            print('\n**********************')
asking()