'''
inheritance : inheritance in which derived class access the properties of base class

1) single inheritance - only one child class is derived from base class
'''

class itvedant:
    def getitv(self):
        self.cname="Itvedant"
    def display(self):
        print("Class name is:",self.cname)

class branch(itvedant):
    def getb(self):
        self.br="Pimpri"

    def displayb(self):
        print("Class name is:",self.cname)
        print("Branch is:",self.br)
        
b=branch()
b.getitv()
b.getb()
b.displayb()
    
        
