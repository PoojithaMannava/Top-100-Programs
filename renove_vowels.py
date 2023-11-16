s=input()
res=""
s=s.lower()
for i in s:
    if i not in "aeiou":
        res=res+i
print(res)
