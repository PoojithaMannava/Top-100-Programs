def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input())
if(n<0):
    print("Factorial For Negative Doesn't exist")
else:
    print(fact(n))
