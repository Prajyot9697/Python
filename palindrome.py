def check_palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return True
    
number=int(input("enter number"))

if check_palindrome(number):
    print("no is palindrome")
else:
    print("no is not palindrome")