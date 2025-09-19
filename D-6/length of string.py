s=input("enter string: ")
l=s.split()
length=0
lword=''
for word in l:
    if len(word)>length:
        length = len(word)
        lword=word
print(length)
print(lword)