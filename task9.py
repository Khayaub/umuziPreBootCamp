X = 3
Y = 5
Z = 1000

x = str(X)
y = str(Y)
z = str(Z)

numsX = list(range(X,Z,X))

numsY = list(range(Y,Z,Y))

numsXY = numsX + numsY #combined list of multiples of 3 and 5 between 0 and 1000

numsXY = list(dict.fromkeys(numsXY)) #remove duplicates e.g. 15,30,45 etc. Multiples of both 3 and 5

Sum = str(sum(numsXY)) #builtin sum function

print("The sum of all multiples of " + x  + " or " + y + " below " + z + " is " + Sum)

