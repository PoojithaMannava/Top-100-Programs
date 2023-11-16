n=int(input())
temp=n
s=0
while temp>0:
    dig=temp%10
    s=s+dig
    temp=temp//10
if(n%s==0):
    print("It's An Harshad Number")
else:
    print("No,It's Not An Harshad Number")
