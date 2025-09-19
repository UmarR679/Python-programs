n = int(input("Enter number: "))
digit_sum = 0
while n:
    d=n%10
    sum=sum+d
    n=n//10
flag=0
for i in range(2,sum):
    if sum%i==0:
        flag+=1
if flag==0:
    print("googly")
else:
    print("not googly")