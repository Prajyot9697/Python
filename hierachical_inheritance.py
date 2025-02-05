'''
hierachical inheritance:

in this only one base class and multiple child class

'''

class Dad:
    def getd(self):
        self.dname=input("Enter Father Name:")

class sis(Dad):
    def gets(self):
        self.sname=input("Enter sister name:")
        
    def displays(self):
        print("Sister Name:",self.sname)
        print("Father Name:",self.dname)
        

class bro(Dad):
    def getb(self):
        self.bname=input("Enter brother name:")

    def displayb(self):
        print("Brother Name:",self.bname)
        print("Father Name:",self.dname)
        
s=sis()
s.getd()
s.gets()
s.displays()

b=bro()
b.getd()
b.getb()
b.displayb()







     
