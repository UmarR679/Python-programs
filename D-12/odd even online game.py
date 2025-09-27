arr = [1,2,3,4,5,6,7,8,9,10]
l=[]
for i in arr:
    if i%2==0:
        l.append(i)
for i in arr:
    if i%2!=0:
        l.append(i)
print(l)

