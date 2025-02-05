#Constructor
'''
constructor is special method
whose name is fixed __init__(self)
constructor is get called automatically at the time of object creation


class student:
    def __init__(self):
        self.n=input("Enter the name:")

    def display(self):
        print("Student name is:",self.n)

s=student()
s.display()'''

class student:
    def __init__(self,age):
        self.n=input("Enter the name:")
        self.a=age

    def display(self):
        print("Student name is:",self.n)
        print("Student age is:",self.a)

s=student(20)
s.display()







































