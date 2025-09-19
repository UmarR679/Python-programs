def even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(even,nums))
print(evens)