arr1=[1,2,6,3,7]
arr2=[10,7,45,3,7]
n=len(arr1)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(n):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
product=1
for i in range(n):
    product+=arr1[i]*arr2[i]
print(product)
            
