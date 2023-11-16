arr=[4,4,5,4,5,1,2,2]
d={}
for i in arr:
    d[i]=d.get(i,0)+1
output=dict(sorted(d.items(),key=lambda x:(-x[1])))
res=[]
for idx,freq in output.items():
    while freq:
        res.append(idx)
        freq=freq-1
print(res)
                   
