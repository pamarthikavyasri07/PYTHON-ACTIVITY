
print("CAMPUS REGISTRATION ID ANALYZER")

student_id = input("Enter Student ID: ").upper()

branches = {
    "CSE": "Computer Science Engineering",
    "ECE": "Electronics and Communication Engineering",
    "EEE": "Electrical and Electronics Engineering",
    "MECH": "Mechanical Engineering",
    "CIV": "Civil Engineering"
}

# Validate student ID
if (len(student_id) == 8 and
    student_id[:2].isdigit() and
    student_id[2:5].isalpha() and
    student_id[5:8].isdigit()):

    year = student_id[:2]
    branch = student_id[2:5]
    roll = student_id[5:8]

    if branch in branches:

        print("\n--- STUDENT DETAILS ---")
        print("Student ID:", student_id)
        print("Admission Year:", "20" + year)
        print("Branch Code:", branch)
        print("Branch Name:", branches[branch])
        print("Student Number:", roll)

    else:
        print("Invalid Branch Code")

else:
    print("Invalid Student ID")

