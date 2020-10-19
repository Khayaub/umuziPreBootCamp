myString1 = input("enter 1st string: " )
myString2 = input("enter 2nd string: " )

combinedString = myString1 + myString2

#print(combinedString)

for letters in combinedString:
    if letters in myString1 and letters in myString2:
        print(letters)
        

