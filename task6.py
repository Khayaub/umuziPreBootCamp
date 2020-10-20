

def maxNum(x,y,z):
    if x > y and x > z:
        maxNum = str(x)
    elif y > x and y > z:
        maxNum = str(y)
    else:
        maxNum = str(z)
    print("The maximum number entered is " + maxNum)

#Test
#maxNum(5,6,7)
#maxNum(9,8,7)
#maxNum(-1,52,759)
#maxNum(-25,-789,52)
#maxNum(-1,-2,-3)
#maxNum(100,-100,100)

