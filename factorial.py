def check_fact(n):
    if n==1:
        return 1
    f=n*check_fact(n-1)
    return f

n=int(input("enter number"))
print("Factorial is:",check_fact(n))