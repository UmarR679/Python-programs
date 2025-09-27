n=22455564634
m=3
s=str(n)
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
res=0
for i in d:
    if d[i]==m:
        res=i
print(res)