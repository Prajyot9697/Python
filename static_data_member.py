class student:
    cls="Itvedant"
    branch="Pimpri"

    def getdata(self):
        self.n=input("enter the name:")
        self.mob=int(input("enter mobile no:"))
        
    def display(self):
        
        print("Student name:",self.n)
        print("Contact number:",self.mob)
        print("Class Name:",self.cls)
        print("Branch name:",self.branch)

s=student()
#s.getdata()
#s.display()
print(type(s))
'''print("class name is:",student.cls)
print("branch name:",student.branch)

student.branch="Pune"

print("class name is:",student.cls)
print("branch name:",student.branch)'''
    
































