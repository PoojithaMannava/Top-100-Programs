arr=[1,2,2,5,5,5,6,7,7]
res=[]
for i in arr:
    if i not in res:
        res.append(i)
    else:
        continue
print(*res)
