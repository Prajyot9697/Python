'''
Multilevel Inheritance

class A   #base class (super class)
   :
   :
class B(A) #interdimate class
   :
   :
class C(B))

'''
'''
class university:
    def getname(self):
        self.name="Pune University"
    def display(self):
        print("University name:",self.name)

class college(university):
    def getcollege(self):
        self.clg="D.Y Patil Management Akurdi"

class Department(college):
        def display(self):
            self.dept="MCA"
            print("University name:",self.name)
            print("College name is:",self.clg)
            print("Department name is:",self.dept)
 
d=Department()

d.getname()
d.getcollege()
d.display()
'''

'''
Create a class called library with data attributes like acc_number, publisher, title

and author. The methods of the class should include

a. read() – acc_number, title, author.

b. compute() - to accept the number of days late, calculate and display the fine

charged at the rate of $1.50 per day.

c. display the data.



class library:
    acc_number=0
    publisher=""
    title=""
    author=""

    def read(self):
        self.acc_number=input("enter account number:")
        self.title=input("enter title:")
        self.author=input("enter author name:")
            
    def compute(self):
        self.no_of_late=int(input("enetr number of days late:"))
        self.fine=self.no_of_late*1.50

    def display(self):
        print("Account Number:",self.acc_number)
        print("Book title:",self.title)
        print("Author Name:",self.author)
        print("No of days late:",self.no_of_late)
        print("Fine Amount:",self.fine)

l=library()

l.read()
l.compute()
l.display()'''



        


    

















































