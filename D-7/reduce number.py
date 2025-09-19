def reduce_to_one(n):
    if n == 1:
        print(1, end=" ")
        return
    print(n, end=" ")
    reduce_to_one(n - 1)

n = int(input("Enter a number: "))
reduce_to_one(n)
