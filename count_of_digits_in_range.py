lower=int(input())
upper=int(input())
d=int(input())
c=0
for num in range(lower,upper+1):
    temp=num
    while temp>0:
        di=temp%10
        if(di==d):
            c=c+1
        temp=temp//10
print(c)
    
