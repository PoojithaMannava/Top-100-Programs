def printdiv(n):
    i=1
    fact=[]
    while i<=n:
        if n%i==0:
            fact.append(i)
        i=i+1
    
    return fact
n=int(input())
print(printdiv(n))
