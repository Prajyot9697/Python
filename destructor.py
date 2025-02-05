''' Destructor method is used to release memory which is used for object creation
destructor name: __del__()
it is called automatically when your entier code is executed'''

class student:
    def __init__(self):
        print("Constructor is called")

    def __del__(self):
        print("Destructor is called")

s=student()



