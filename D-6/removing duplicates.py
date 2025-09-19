s = input("Enter a string: ")
new_s = ""
for ch in s:
    if ch not in new_s:
        new_s += ch
print("String without duplicates:", new_s)
