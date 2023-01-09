
class details:
    def __init__(self):
        self.id="<NO ID>"
        self.name="<NO NAME>"
        self.gender="<NO GENDER>"

    def setdata(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender

    def showdata(self):
        print("ID ",self.id)
        print("NAME ",self.name)
        print("GENDER ",self.gender)

class employee(details):
    def __init__(self):
        self.company="<NO COMPANY>"
        self.dept="<NO DEPT>"

    def setemployee(self,id,name,gender,comp,dept):
        self.setdata(id,name,gender)
        self.company=comp
        self.department=dept

    def showemployee(self):
        self.showdata()
        print("COMPANEY :",self.company)
        print("DEPARTMENT :",self.department)

class doctor(employee):
    def __init__(self):
        self.hospital="<NO HOSPITAL>"
        self.dept="<NO DEPT>"

    def setdoctor(self,id,name,gender,hospital,dept):
        self.setdata(id,name,gender)
        self.hospital=hospital
        self.dept=dept

    def showdoctor(self):
        self.showdata()
        print("HOS{ITAL :",self.hospital)
        print("DEPARTMENT :",self.dept)

print("Employee Object")
c1=employee()
c1.setemployee(1,"PARTH","MALE","TOPS","DEVLOPER")
c1.showemployee()

print("\nDoctor Object")
d1=doctor()
d1.setdoctor(2,"HARSH","MALE","ZYDUS","ETE SPECIALIST")
d1.showdoctor()