def reverse_integer(n, rev=0):
    if n == 0:
        return rev
    return reverse_integer(n // 10, rev * 10 + n % 10)

n = int(input("Enter an integer: "))
print("Reversed:", reverse_integer(n))
