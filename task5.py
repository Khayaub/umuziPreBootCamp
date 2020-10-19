
num1 = int(input("enter 1st side length: "))
num2 = int(input("enter 2nd side length: "))
num3 = int(input("enter 3rd side length: "))

semiP = (num1 + num2 + num3) / 2
areaSq = semiP * (semiP - num1) * (semiP - num2) * (semiP - num3)
area = str(areaSq**0.5)

print("The area of your triangle is " + area " sq units")
