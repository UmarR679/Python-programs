n =int(input("enter num: "))
while n>9:
    sum=0
    while n>0:
        d=n%10
        sum+=d
        n//=10
    n=sum
if n==1:
    print("magic number")
else:
    print("not magic number")