def fibonacii(n):
    if n<=1:
        return n
    else:
        return fibonacii(n-1)+fibonacii(n-2)
n=int(input())
if n<=0:
    print("Please Enter A Positive Number:")
else:
    print("Fibonacii terms",end=" ")
    for i in range(n):
        print(fibonacii(i),end=" ")
        
