# report_card
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Report Card ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)