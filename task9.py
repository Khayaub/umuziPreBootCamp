
def sumUntil(x,y,z):
    numbersX = list(range(x,z,x))
    numbersY = list(range(y,z,y))

    numbersXY = numbersX + numbersY
    numbersXY = list(dict.fromkeys(numbersXY))
    Sum = str(sum(numbersXY))

    print("The sum of all natural number multiples of " + str(x) + " and "
          + str(y) + " below " + str(z) + " is " + Sum)
    
sumUntil(3,5,10)

#Test    
#sumUntil(3,5,1000)
#sumUntil(2,3,10)
