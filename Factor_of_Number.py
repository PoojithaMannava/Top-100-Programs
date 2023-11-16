n=int(input())
fact=[]
for i in range(1,n+1):
    if(n%i==0):
        fact.append(i)
print(*fact)
