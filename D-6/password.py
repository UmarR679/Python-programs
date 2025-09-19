password = input("Enter the password: ")
uc,lc,d,sp,cc=1,1,1,1,0
sp_count = 0
fc=0
c=0
l=len(password)
if not l>=6 and l<22:
    c=1
for i in range(l):
    if  password[i].isupper():
        uc=0
    if password[i].islower():
        lc=0
    if password[i].isdigit():
        d=0
    if password[i] in "!@#$%^&*":
        sp_count+=1
    if sp_count>=2:
        sp=0
    if i+1<l and password[i]==password[i+1]:
        cc=1
fc+=uc+lc+d+sp+cc+c
print(fc)