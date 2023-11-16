def is_perfect(n):
    i=1
    while i*i<=n:
        if i*i==n:
            return true
        i=i+1
    return False
print(is_perfect(n))
