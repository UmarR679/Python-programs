# s=input()
# s=s.replace(" ","-")
# print(s)

#without replace method
s = input("Enter a string: ")
s1 = ""
for ch in s:
    if ch.isspace():
        s1+=""
    else:
        s1+=ch
