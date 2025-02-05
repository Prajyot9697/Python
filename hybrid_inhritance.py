'''
hybrid inheritance

it is combination of multiple and hierachical inheritance

'''
'''
class Library:
    def getl(self):
        self.lname=input("Enter Library name=")

class Book(Library):
    def getb(self):
        self.bname=input("Enter Book Name=")
        

class Author(Library):
    def geta(self):
        self.aname=input("Enter Author Name=")
    


class Show(Book,Author):
    
    def displays(self):
        print("Library Name=",self.lname)
        print("Book Name=",self.bname)
        print("Author Name=",self.aname)


s=Show()

s.getl()
s.getb()
s.geta()
s.displays()
'''



class a:
   def geta(self):
        self.a=int(input("Enetr value of a="))

class b:
    def getb(self):
        self.b=int(input("Enter value of b="))

class Add(a,b):
    def add(self):
        self.c=self.a+self.b

class math(Add):
    
    def display(self):
        print("Addition of two numbers=",self.c)

class show(Add):

    def show(self):
        print("value of a=",self.a)
        print("value of b=",self.b)
        print("Addition is=",self.c)


s=show()
s.geta()
s.getb()
s.add()
s.show()


    
    


































