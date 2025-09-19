n = int(input("enter number: "))
if n<=1:
    print("not a composite number")
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
        c+=1
if c>2:
    print("composite")
else:
    print("not composite")
