
class tops:
  def __init__(self):
    print("welcome to tops!")

class branch():
    def __init__(self, branch):
        print("welcome to " + branch + "!")

class student():
   def __init__(self):
     self.id = int(input("Enter A Id :"))
     self.name = input("Enter A Name :")
     self.state = input("Enter A State :")
     self.cust= input("Enter A Current Study :")

     print("\nID :",self.id)
     print("Name :",self.name)
     print("State :",self.state)
     print("Current Std :",self.cust)
     print("We Have 3 Course {python,da,java}")

   def coursedetails(self,course):
    self.course=input("Enter A course :")

    if (course == "python"):
      print("You Selected Python Course")
      print("the faculty for python is jigar sir")
      print("Python Course Duration 6 to 8 Months")
      print("Python Course Fees : 40000")
    elif (course == "da"):
      print("You Selected DA Course")
      print("the faculty for da is khushbu maam")
      print("da Course Duration 5 to 7 Months")
      print("Python Course Fees : 45000")
    elif(course== "java"):
      print("You Selected Java Course")
      print("the faculty for java is param sir")
      print("java Course Duration 8 to 8 Months")
      print("Python Course Fees : 50000")

a=tops()
b=branch("S G highway")

c=student()
c.coursedetails("python")

d=student()
d.coursedetails("da")

e=student()
e.coursedetails("java")