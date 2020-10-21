
def celsiusToFah(x):
    degreesFah = str((x *9/5) + 32)
    print("The temperatur in degrees Fahrenheit is " + degreesFah)

def fahToCelsius(y):
    degreesCel = str((y - 32) * 5/9)
    print("The temperature in degrees celsius is " + degreesCel)

celsiusToFah(0)
fahToCelsius(0)

#Test
#celsiusToFah(-36)
#celsiusToFah(100)
#fahToCelsius(-36)
#fahToCelsius(100)
