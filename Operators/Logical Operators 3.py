a=int(input("Year = "))
if (a%400==0) or ((a%4==0) and (a%100!=0)) :
    print("It is a leap year")
else:
    print("It is not a leap year")
