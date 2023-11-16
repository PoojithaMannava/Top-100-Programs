arr=[1,34,567,89,900]
s=float('inf')
ss=float('inf')
l=float('-inf')
sl=float('-inf')
for i in range(len(arr)):
    if(arr[i]>l):
        sl=l
        l=arr[i]
    elif(arr[i]>sl and arr[i]!=l):
        sl=arr[i]
for i in range(len(arr)):
    if arr[i]<s:
        ss=s
        s=arr[i]
    elif(arr[i]<ss and arr[i]!=s):
        ss=arr[i]
print("second largest element is:",sl)
print("second smallest elemen is:",ss)
