n = int(input("Enter number: "))
if n<=1:
    print("not perfect number")
else:
    sum_div=0
    for i in range(1,n):
        if n%i==0:
            sum_div += i
            print(i)
    print("sum: ",sum_div)
    if n==sum_div:
        print("perfect num")
    else:
        print("not perfect")
