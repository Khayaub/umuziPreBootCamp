myString = input("enter a string: " )

for letter in myString:
    if letter in 'aeiou' or letter in 'AEIOU':
        print(letter)
