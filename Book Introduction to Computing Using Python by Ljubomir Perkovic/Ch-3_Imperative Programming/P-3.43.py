print('Problem 3.43')

def hit(x,y,r,Xp,Yp):
    import math
    point = math.sqrt((x-Xp)**2 + (y-Yp)**2)
    if point <= r:
        print(True)
    else:
        print(False)
    

    
        

        
