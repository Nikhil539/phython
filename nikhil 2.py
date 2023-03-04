year=int(input("enter year"))
if year%4==0 or year%400==0:
    print("leap year")
else:
    print ("Not a leap year")
