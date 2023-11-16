n=int(input())
temp=n
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
print(rev)
    
