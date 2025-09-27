arr=[10,11,7,12,14]
total = sum(abs(arr[i] - arr[i+1]) for i in range(len(arr) - 1))
print(total)