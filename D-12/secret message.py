text = input("enter string: ")
count=0
for i in text:
    if not i.isalnum():
        count+=1
print(count)