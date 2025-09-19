lst=list(map(int,input("enter the list: ").split()))
lst1=[]
for i in lst:
    if lst.count(i)%2!=0 and i not in lst1:
        lst1.append(i)
print(lst1)