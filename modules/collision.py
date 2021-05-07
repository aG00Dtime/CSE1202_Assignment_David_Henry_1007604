import math

def hit(x1,y1,x2,y2,space):
    distance=  math.sqrt(((x2-x1)**2)+((y2-y1)**2)) 
    if distance <= space:
        return True

