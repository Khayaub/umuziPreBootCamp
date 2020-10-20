
def commonLetters():
    string1 = input("Enter 1st string: ")
    string2 = input("Enter 2nd string: ")
    combinedString = string1 + string2

    for letters in combinedString:
        if letters in string1 and letters in string2:
            print(letters)

commonLetters()
