def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(f"{n} is Prime" if is_prime(n) else f"{n} is Not Prime")
