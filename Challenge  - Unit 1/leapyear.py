def CheckLeap(Year):
    # checking if the given year is leap year
    if((Year % 400 == 0) or
       (Year % 100 != 0) and
       (Year % 4 == 0)):
      print("given year is a leap year")
    #else it is not a leap year
    else:
        print ("given year is not a leap year")
#taking an input year from user
Year = int(input("enter the number: "))
#printing result
CheckLeap(Year)  |