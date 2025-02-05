'''
Multiple inheritance:

in which child class can have many Parent(base) class

   A     B    C
   :     :    :
   ____________
         :
         D(A,B,C)

'''

class dad:
    def getd(self):
        self.dname=input("Enter the father name:")

class Mom:
    def getm(self):
        self.mname=input("Enter the mother name:")

class child(dad,Mom):
    def getc(self):
        self.cname=input("Enter the child name:")

    def display(self):
        print("Student Name:",self.cname)
        print("Father Name:",self.dname)
        print("Mothet Name:",self.mname)

c=child()
c.getd()
c.getm()
c.getc()
c.display()








































