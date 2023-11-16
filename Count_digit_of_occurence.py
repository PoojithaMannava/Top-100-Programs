n=int(input())
d=int(input())
temp=n
c=0
while temp>0:
    di=temp%10
    if(d==di):
        c=c+1
    temp=temp//10
print(c)
