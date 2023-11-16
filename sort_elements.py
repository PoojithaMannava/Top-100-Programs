arr=[4,3,2,1]
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if(arr[j]>arr[i]):
            temp=arr[j]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
            
