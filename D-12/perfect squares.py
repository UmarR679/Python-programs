areas = [4,9,36,7,2]
count=0
for a in areas: 
    i = 1
    while i * i <= a:
        if i * i == a:
            count += 1
            break
        i += 1
print(count)