def fibonacii(n):
    if n<=1:
        return n
    else:
        return fibonacii(n-1)+fibonacii(n-2)
n=int(input())
if n<=0:
    print("Wrong Input")
else:
    print(fibonacii(n))
