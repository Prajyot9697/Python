def prime(n):
    for i in range(2,n):
        if n%i==0:
            return True
        
n=int(input("enter number"))

if prime(n):
    print("no is not prime")
else:
    print("no is prime")