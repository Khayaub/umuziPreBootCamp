def areaOfTriangle(x,y,z):
    semiP = (x + y + z)/2
    area = str((semiP * (semiP - x) * (semiP - y) * (semiP - z))**0.5)
    print("The area of your triangle is " + area + " sq units")

areaOfTriangle(3,4,5)

#Test
#areaOfTriangle(50,40,30)
#areaOfTriangle(15,75,69)
