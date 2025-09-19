numbers = [0, 1, 2, 3, 4, 5, 16, 23, 42, 99]

for num in numbers:
    if num & 1 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
