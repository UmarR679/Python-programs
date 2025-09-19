num = int(input("enter num: "))
sum=0
mul=1
while num>0:
    d=num%10
    sum+=d
    mul*=d
    num=num//10
if sum == mul:
    print("spy")
else:
    print("not spy")