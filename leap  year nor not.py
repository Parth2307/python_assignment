year=int(input("Enter A Year"))

if(year%400==0):
    print(year,"Is Leap Year")
elif(year%100==0):
    print(year,"Is Leap Year")
elif(year%4==0):
    print(year,"Is leap Year")
else:
    print(year,"Is Not leap Year")