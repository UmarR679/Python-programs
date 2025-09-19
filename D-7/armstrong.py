def is_armstrong(num):
    power = len(str(num))
    total = sum(int(d)**power for d in str(num))
    return total == num

n = int(input("Enter a number: "))
print(f"{n} is Armstrong" if is_armstrong(n) else f"{n} is Not Armstrong")
