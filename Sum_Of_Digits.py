n=int(input())
s=0
temp=n
while temp>0:
    dig=temp%10
    s=s+dig
    temp=temp//10
print(s)
