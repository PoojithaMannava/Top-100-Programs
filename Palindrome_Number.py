n=int(input())
temp=n
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if(rev==n):
    print("It's A Palindrome")
else:
    print("It's Not A Palindrome")
    
