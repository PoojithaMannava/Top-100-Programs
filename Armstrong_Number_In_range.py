m=int(input())
n=int(input())
res=[]
for i in range(m,n+1):
    temp=i
    s=0
    l=len(str(temp))
    while temp>0:
        d=temp%10
        s=s+d**l
        temp=temp//10
    if(s==i):
        res.append(i)
print(*res)
