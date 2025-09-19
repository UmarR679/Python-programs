n = int(input("Enter number: "))
temp1 = n
temp2 = n
c=0
while temp1>0:
    c+=1
    temp1=temp1//10
arm=0
while temp2>0:
    d=temp2%10
    arm=arm+d**c
    temp2=temp2//10
if arm==n:
    print("armstrong")
else:
    print("not armstrong")
