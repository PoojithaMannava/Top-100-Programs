arr=[1,2,2,3,4,4]
d={}
for i in arr:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d:
    if d[i]>=2:
        print(i)
        
