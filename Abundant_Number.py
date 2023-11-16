n=int(input())
temp=str(n)
square=n**2
b=str(square)
if b.endswith(temp):
    print("yes,it's an automorphiic number")
else:
    print("no")
