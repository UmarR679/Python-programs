def nums(n):
    if n == 1:
        print(1, end=" ")
        return
    nums(n - 1)
    print(n, end=" ")
n = int(input())
nums(n)