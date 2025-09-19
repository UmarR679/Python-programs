# s=input("enter string: ")
# s=s.title()
# print(s)

#second approach
s=input("enter string: ")
words = s.split()
res=''
for word in words:
    cap=word[0].upper()+word[1:]
    res=res+' '+cap
print(res)