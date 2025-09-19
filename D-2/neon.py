num=int(input("enter number: "))
sqr=num*num
sum=0
while sqr>0:
    d=sqr%10
    sum=sum+d
    sqr=sqr//10
if sum==num:
    print("neon")
else:
    print("not neon")