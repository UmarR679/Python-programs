def check_square(n, i=1):
    if i * i == n:
        return True
    if i * i > n:
        return False
    return check_square(n, i + 1)

n = int(input("Enter a number: "))
if check_square(n):
    print(n, "is a Perfect Square")
else:
    print(n, "is NOT a Perfect Square")
