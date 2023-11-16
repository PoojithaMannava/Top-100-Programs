s=input()
res=""
for i in s:
    if i.isupper():
        i=i.lower()
        res=res+i
    else:
        if i.islower():
            i=i.upper()
            res=res+i
print("string after toggling is:",res)
#we can use swapcase also
