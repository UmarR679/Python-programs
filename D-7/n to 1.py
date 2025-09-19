def nums(n):
    if n == 1:
        print(1, end=" ")
        return
    print(n, end=" ")
    nums(n - 1)
n = int(input())
nums(n)