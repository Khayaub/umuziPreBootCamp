def areaOfTriangle(x,y,z):
    semiP = (x + y + z)/2
    area = str((semiP * (semiP - x) * (semiP - y) * (semiP - z))**0.5)
    print("The area of your triangle is " + area + " sq units")

#Test
#areaOfTriangle(3,4,5)
#areaOfTriangle(50,40,30)
#areaOfTriangle(15,75,69)
