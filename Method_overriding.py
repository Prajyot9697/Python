'''
class A:
    def __init__(self):
        print("inside class A constructor")

class B(A):
    
    def __init__(self):
        super().__init__()
        print("inside class B constructor")
                        
b=B()
'''

class a:
    def get(self):
        self.a=int(input("enter value of a="))

class b(a):
    
    def get(self):
        super().get()
        self.b=int(input("enter value of b="))
        self.c=self.a+self.b

    def display(self):
        print("Addition is:",self.c)


be=b()
be.get()
be.display()

