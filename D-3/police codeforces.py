n = int(input())
events = list(map(int, input("Enter list: ").split()))

available_officers = 0
untreated = 0

for event in events:
    if event == -1:
        if available_officers > 0:
            available_officers -= 1
        else:
            untreated += 1
    else:
        available_officers += event

print(untreated)
