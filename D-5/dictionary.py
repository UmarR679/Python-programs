student_marks = {
    'sita': 95,
    'aakash': 88,
    'anvesh': 56,
    'honey': 41,
    'mallesh': 15,
    'arjun': 54,
    'mani': 29
}
for name in student_marks:
    marks = student_marks[name]

    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    elif marks >= 35:
        grade = 'D'
    else:
        grade = 'F'

    print(name, "grade", grade)
