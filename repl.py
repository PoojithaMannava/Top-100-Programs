s=input()
s=list(s)
for i in range(len(s)):
    if(s[i]=="?"):
        s[i]="a"
    if(s[i]==s[i+1]):
        s[i+1]=chr(ord(s[i])+1)
    if(s[i]==s[i-1]):
        s[i-1]=chr(ord(s[i])-1)
print("".join(s))
        
