age = int(input("enter age: "))
if age < 18:
    print("not allowed")

if age >= 18:
    print("allowed")
elif age >= 75:
    print("risk for life")
elif age >= 45:
    print("panic attack")
elif age >= 25:
    print("don't make nonsense")
else:
    print("don't scream")

