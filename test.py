'''
def prime(n):
    if n>0:
        for i in range(2,n-1):
            if n%i==0:
                return True
                
n=int(input("enter number:"))
if prime(n):
    print("not prime number")
else:
    print("prime number")
'''
    
'''
n=int(input("enter number="))

def fact(n):
    if n==1:
        return 1
    f=n*fact(n-1)
    return f
print(fact(n))
'''    

'''
n=int(input("enter number="))

a=n%10
b=n//10
c=b%10
d=b//10
result=a+c+d
print(result)
a=a*100
c=c*10
d=d*1
res=a+c+d
print(res)
'''
'''
def count_letter(s):
    letter_count={}

    for letter in s:
        if letter in letter_count:
            letter_count[letter]+=1
        else:
            letter_count[letter]=1
    return letter_count

inp_string='madam'
result=count_letter(inp_string)
print(result)
 '''   


letter_count={}
print(type(letter_count))







































    
        
    





    
    

    



