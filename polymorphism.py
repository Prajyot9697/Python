'''
Operator Overloading is way to implement polymorphism
'''
'''
a='10'
b='20'
print(a+b)

a=10
b=20
print(a+b)


special methods: call when there is operator



a=10
b=20
c=a+b
d=int.__add__(a,b)

print("Addition of",a,"and",b,"is:",c)
print("Addition of",a,"and",b,"is:",d)



class student:
    def get(self):
        self.m=int(input("Enter the mark:"))

    def __add__(x,y):
        t=student()
        t.m=x.m+y.m
        return t

    def display(self):
        print("Addition of marks is:",self.m)


s=student()
s1=student()
s.get()
s1.get()
s3=s+s1
s3.display()


class student:
    def get(self):
        self.m=int(input("Enter the mark:"))

    def __add__(x,y):
        return x.m+y.m

s=student()
s1=student()
s.get()
s1.get()
print("Addition of marks is:",s+s1)

'''

class emp:
    def __init__(self,name,sal):
        self.n=name
        self.s=sal
    def __mul__(e,h):
        return e.s*h.p     

class HR:
    def __init__(self,days):
        self.p=days

   
e=emp('Prajyot',500)
h=HR(20)
print("Total Salary of",e.n,"is:",e*h)





















































































