print("Problem 3.37")

def points(x1,y1,x2,y2):
    import math
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("The distance :", d, "unit")
    if (x2-x1) !=0:
        m = ((y2-y1)/(x2-x1))
        print("The slope: ", m)
    else:
        print("The slopes is infinity")
        
    
        
