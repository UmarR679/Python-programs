def update(n):
    return n*2
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(update,evens))
print(doubles)