m=int(input())
n=int(input())
gcd=1
for i in range(1,min(m,n)):
    if(m%i==0 and n%i==0):
        gcd=i
print(gcd)
