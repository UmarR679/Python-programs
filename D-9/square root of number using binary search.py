n=16
low, high = 0,n
result = 0
while low<= high:
    mid=(low+high)//2
    if mid * mid <= n:
        result=mid
        low=mid+1
    else:
        high=mid-1
print(result)