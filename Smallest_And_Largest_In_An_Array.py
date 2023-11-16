arr=[1,456,9,89]
maxi=arr[0]
mini=arr[0]
for i in range(len(arr)):
    if(arr[i]<mini):
        mini=arr[i]
    if(arr[i]>maxi):
        maxi=arr[i]
print("The Maximum Element Is:",maxi)
print("The Minimum Element Is:",mini)
