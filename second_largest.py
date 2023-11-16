arr=[1,4,677,89]
l=arr[0]
sl=arr[0]
for i in range(len(arr)):
    if(arr[i]>l):
        sl=l
        l=arr[i]
    elif(arr[i]>sl and arr[i]!=l):
        sl=arr[i]
print("Second Largest Element is:",sl)
