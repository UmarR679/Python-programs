s = input("Enter text: ")
stack = []
for i in s:
    if i == "*":
        if stack:
            stack.pop()
    else:
        stack.append(i)
result="".join(stack)
print(result)