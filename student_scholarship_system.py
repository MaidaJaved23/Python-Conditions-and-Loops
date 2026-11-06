# Student Scholarship Eligibility System
# Demonstrates if, elif, else, input validation, and decision-making.

print("===== STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM =====")

# Collect and validate the student's name.
while True:
    student_name = input("Enter student name: ")
    if student_name:
        break
    print("Error: Student name cannot be empty.")

# Collect and validate academic marks.
while True:
    try:
        academic_marks = float(input("Enter academic marks percentage (0-100): "))
        if 0 <= academic_marks <= 100:
            break
        print("Error: Academic marks must be between 0 and 100.")
    except ValueError:
        print("Error: Please enter a valid numeric marks percentage.")

# Collect and validate attendance percentage.
while True:
    try:
        attendance_percentage = float(
            input("Enter attendance percentage (0-100): ")
        )
        if 0 <= attendance_percentage <= 100:
            break
        print("Error: Attendance must be between 0 and 100.")
    except ValueError:
        print("Error: Please enter a valid numeric attendance percentage.")

# Collect and validate monthly family income.
while True:
    try:
        monthly_family_income = float(
            input("Enter monthly family income (Rs.): ")
        )
        if monthly_family_income >= 0:
            break
        print("Error: Family income cannot be negative.")
    except ValueError:
        print("Error: Please enter a valid numeric family income.")

# Evaluate each eligibility requirement and record every reason for ineligibility.
ineligibility_reasons = []

if academic_marks < 80:
    ineligibility_reasons.append("Academic marks are below 80%.")

if attendance_percentage < 85:
    ineligibility_reasons.append("Attendance is below 85%.")

if monthly_family_income > 50000:
    ineligibility_reasons.append("Monthly family income is above Rs. 50,000.")

# Determine the scholarship result.
if not ineligibility_reasons:
    if academic_marks >= 90:
        scholarship_status = "Full Scholarship"
    elif academic_marks >= 80:
        scholarship_status = "Partial Scholarship"
    else:
        # This branch is a defensive fallback; eligible marks are at least 80%.
        scholarship_status = "Not Eligible"
else:
    scholarship_status = "Not Eligible"

# Display the complete evaluation report.
print("\n===== SCHOLARSHIP EVALUATION REPORT =====")
print(f"Student Name: {student_name}")
print(f"Academic Marks: {academic_marks:.2f}%")
print(f"Attendance: {attendance_percentage:.2f}%")
print(f"Monthly Family Income: Rs. {monthly_family_income:,.2f}")
print(f"Scholarship Result: {scholarship_status}")

if ineligibility_reasons:
    print("\nReason(s) for Ineligibility:")
    for reason in ineligibility_reasons:
        print(f"- {reason}")
else:
    print("Eligibility Status: All scholarship requirements are satisfied.")

print("=========================================")
