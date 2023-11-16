m=int(input())
n=int(input())
if m<n:
    smaller=m
else:
    smaller=n
for i in range(1,smaller+1):
    if(m%i==0 and n%i==0):
        hcf=i
print(hcf)
        
