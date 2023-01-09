

num=int(input("Enter A Number "))

if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
             print("Number Is Not Prime")
             break

    else:
        print("Number Is Prime")
else:
    print("Number Is Not Prime")


