n = int(input("Enter a number: "))

sum_digits = 0
temp = n
while temp > 0:
    sum_digits += temp % 10   # extract last digit
    temp //= 10               # remove last digit

if n % sum_digits == 0:
    print("Niven Number")
else:
    print("Not a Niven Number")
