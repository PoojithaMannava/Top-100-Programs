arr=[1,2,4,7,7,5]
s=float('inf')
ss=float('inf')
for i in range(len(arr)):
    if(arr[i]<s):
        ss=s
        s=arr[i]
    elif(arr[i]<ss and arr[i]!=s):
        ss=arr[i]
print(ss)
