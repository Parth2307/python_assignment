class boss():
    def __init__(self):
        print("Hello , I am Boss")

    def sername(self):
        print("i am founder of")

class emy(boss):
    def __init__(self):
        super().__init__()
        print("Hi I am emy")

    def show(self):
        print("My sellar is:")

a1=boss()   
a1.sername()

b1=emy()
b1.show()
