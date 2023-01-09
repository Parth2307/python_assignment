#parent class
class student():
    def __init__(self):
        print("I am parent class constructor")

    def display(self):
        print("I am parent class display method")

    def calculate(self,a,b,c):

        self.a=a
        self.b=b
        self.c=c
        self.s=a+b+c

        print("Sum Of Three Numbers ",self.s)


#child class

class student_child(student):
    def __init__(self):
        #call the parent(super) function
        super().__init__()
        print("I am child class constructor")

    def show(self):
        print("I am show method of child class")

#creating the instance/object of the child/derived class

x=int(input("Enter A First Number: "))
y=int(input("Enter A Second Number: "))
z=int(input("Enter A Third Number: "))

c1=student_child()

c1.calculate(x,y,z)
c1.display()
c1.show()



