num1 = int(input())
num2 = int(input())
sumNums = str(num1 + num2)

#print(sumNums), printed sumNums for testing

if (num1 or num2 == 3) and ('3' in sumNums):
    print("True")
else:
    print("False")
