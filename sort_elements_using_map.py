arr=[1,1,1,1,1,3,3,3,4,4,4,8]
d={}
for i in arr:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
n=len(arr)
for i in range(n):
    for j in range(i,n):
        if(d[arr[i]]>d[arr[j]]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
            
