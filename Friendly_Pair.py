m=int(input())
n=int(input())
s1=0
s2=0
for i in range(1,m+1):
    if m%i==0:
        s1=s1+i
for i in range(1,n+1):
    if n%i==0:
        s2=s2+i
if s1/m==s2/n:
    print("Yes,It's A Friendly Pair")
else:
    print("No,it's Not A Frendly Pair")
