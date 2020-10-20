def minutesToHours(x):
    hours = x//60
    minutes = x%60
    numAns = str(x)

    print(numAns + " minutes converts to " + str(hours) + " hour(s) and "
          + str(minutes) + " minutes ")



# Test  
#minutesToHours(71)
#minutesToHours(133)
#minutesToHours(58)
#minutesToHours(240)
#minutesToHours(90)
#minutesToHours(999)
