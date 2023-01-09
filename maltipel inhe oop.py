
class  operation1():
    def sum(self,a,b):
        print("Sum Of A and B:",a+b)

class  operation2():
    def multi(self,a,b):
        print("Multiphication Of A and B :",a*b)

class  operation3():
    def substract(self,a,b):
        print("Substraction Of A and B:",a-b)

class  operation4():
    def division(self,a,b):
        print("Division Of A and B :",a/b)

class  operation5( operation1, operation2, operation3, operation4):
    def mod(self,a,b):
        print("Mod OF A and B :",a%b)     

claculate=operation5()

a=int(input("Enter Value Of A :"))
b=int(input("Enter Value Of B :"))

claculate.sum(a,b)
claculate.multi(a,b)
claculate.substract(a,b)
claculate.division(a,b)
claculate.mod(a,b)
