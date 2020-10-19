
num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
sumNums = str(num1 + num2)

#print(sumNums), printed sumNums for testing

if (num1 or num2 == 3) and ('3' in sumNums):
    print("True")
else:
    print("False")
