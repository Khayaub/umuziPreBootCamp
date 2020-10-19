
num1 = int(input("enter number of minutes: "))

hours = num1//60
minutes = num1%60

numAns = str(num1)

print(numAns + " minutes converts to " + str(hours) + " hour(s) and " + str(minutes) + " minutes")
