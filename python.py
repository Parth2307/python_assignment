class calculator_implementation():
   def __init__(self,in_1,in_2):
      self.a=in_1
      self.b=in_2
   def add_vals(self):
      return self.a+self.b
   def multiply_vals(self):
      return self.a*self.b
   def divide_vals(self):
      return self.a/self.b
   def subtract_vals(self):
      return self.a-self.b
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))
print("The entered first and second numbers are : ")
print(input_1, input_2)
my_instance = calculator_implementation(input_1,input_2)
choice=1
while choice!=0:
   print("0. Exit")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   choice=int(input("Enter your choice... "))
   if choice==1:
      print("The computed addition result is : ",my_instance.add_vals())
   elif choice==2:
      print("The computed subtraction result is : ",my_instance.subtract_vals())
   elif choice==3:
      print("The computed product result is : ",my_instance.multiply_vals())
   elif choice==4:
      print("The computed division result is : ",round(my_instance.divide_vals(),2))
   elif choice==0:
      print("Exit")
   else:
      print("Sorry, invalid choice!")
print()
print("-----------------------------------------------------------------------------------------")




class Calculator:
    def addition(self):
        print(a + b)
    def subtraction(self):
        print(a - b)
    def multiplication(self):
        print(a * b)
    def division(self):
        print(a / b)
a = int(input("Enter first number:"))
b = int(input("Enter first number:"))
obj = Calculator()

obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()

