num=int(input("enter number: "))
org_num=num
fact=1
sum=0
while num>0:
    d=num%10
    for i in range(1,d+1):
        fact = fact*i
    sum=sum+fact
    num=num//10
    fact=1
if org_num==sum:
    print("strong num")
else:
    print("not strong")