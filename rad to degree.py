#Convert radians to degree 1rad × 180/π = 57.296°
#Receive Input rad
#Multiply rad by 180
#Divide product by pi
#Print result
#import math library

def radconv():
    import math
    inp= float(input('Please enter number to be converted '))
    pi=math.pi
    prod = inp*180
    result=prod/pi
    print(result)
    return
radconv()

