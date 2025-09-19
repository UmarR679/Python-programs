t = (1, 2, 3, 2, 4, 5, 1, 6, 3, 2)

count = {}
for item in t:
    count[item] = count.get(item, 0) + 1

repeated = [k for k, v in count.items() if v > 1]

print("Repeated elements:", repeated)
