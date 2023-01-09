
class grandfather :
    def speak(self):
        print("Grand Father Speaks True")
    def color(self):
        print("Grand Father Color is White")
    def thought(self):
        print("Grand father behaviour is simple and cool")

class father(grandfather):
    def education(self):
        print("My Father Is B.tech Graduate")

class son(father):
    def height(self):
        print("This son height Is 6 fit")

s1=son()

s1.speak()
s1.color()
s1.thought()
s1.education()
s1.height()