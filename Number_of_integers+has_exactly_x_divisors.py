n=int(input())
x=2
c0=0
for i in range(1,n+1):
    cf=0
    for j in range(1,i+1):
        if(i%j==0):
            cf=cf+1
    if cf==x:
        c0+=1
print(c0)
    
