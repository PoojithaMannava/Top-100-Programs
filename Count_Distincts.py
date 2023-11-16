arr=[10,20,40,30,50,20,10,20]
d={}
for i in arr:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(len(d))
