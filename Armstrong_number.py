n=int(input())
temp=n
l=len(str(n))
s=0
while temp>0:
    dig=temp%10
    s=s+dig**l
    temp=temp//10
if(s==n):
    print("It's An Armstrong Number")
else:
    print("It's Not An Armstrong Number")
