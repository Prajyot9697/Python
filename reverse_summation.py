n=int(input("enter number"))

a=n%10
b=n//10
c=b%10
d=b//10

result=a+c+d

print("Addition of digit=",result)

a=a*100
c=c*10
d=d*1

res=a+c+d

print("Reverse number=",res)