'''
oops pillars
1) Abstraction - hiding unneccesary deatils showing only nessecary details
2) encapsulation - mechanism is of wrapping the data in single unit e.g class
'''

class student:
    branch="Pimpri"  # private access specifier __branch
    def getdata(self,name,age):
        self.n=name
        self.a=age
        self.__display()  #__display(self)
       
    def __display(self):  #self=self
        print("Student name:",self.n)
        print("Student age:",self.a)
        print("Branch name:",self.branch)
        
s=student()
s.getdata("Hardik",20)
#s.display()
#print(student.branch)
