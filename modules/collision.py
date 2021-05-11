# import math function
import math


# check distance between two objects
def hit(x1, y1, x2, y2, space):
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    # print(distance)
    if distance <= space:
        return True
