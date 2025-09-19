def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

n = int(input("Enter a number: "))
print(f"{n} is Perfect" if is_perfect(n) else f"{n} is Not Perfect")
