
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks: "))

    subjects = int(input("Enter number of subjects: "))
    subject_marks = []

    for j in range(subjects):
        m = float(input("Enter subject marks: "))
        subject_marks.append(m)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if (marks >= 75 and
        all(m >= 50 for m in subject_marks) and
        attendance >= 75 and
        income <= 250000):

        students.append([name, marks, attendance, income])
        print("Eligible")
    else:
        print("Not Eligible")

# Ranking based on marks, attendance and income
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- SCHOLARSHIP RANK LIST ---")

if students:
    for rank, s in enumerate(students, 1):
        print(rank, s[0], s[1], s[2], s[3])
else:
    print("No eligible students found")

