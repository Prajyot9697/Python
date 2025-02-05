class A:
    def __init__(self):
        print("inside class A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("inside class B constructor")
        
b=B()
