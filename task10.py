

def onlyVowels():
    myString = input("Enter a string: ")
    for letter in myString:
        if letter in "aeiou" or letter in "AEIOU":
            print(letter)

onlyVowels()
    
