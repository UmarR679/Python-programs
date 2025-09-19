lst=list(map(int,input("enter the list: ").split()))
lst.sort()
print(sum(lst[:3]))