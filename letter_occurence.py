def letter_occurrenece(s):
    letter_count={}

    for letter in s:
        if letter in letter_count:
            letter_count[letter]+=1
        else:
            letter_count[letter]=1
    return letter_count

n=input("enter string=")
 
result=letter_occurrenece(n)
print(result)
