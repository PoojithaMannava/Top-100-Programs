m=int(input())
n=int(input())
res=[]
for i in range(m,n+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if c==2:
        res.append(i)
print(*res)
