students = {
    "Asha": "Python",
    "Ravi": "Data Analytics",
    "Neha": "AI"
}

print("Students:")
for name in students.keys():
    print(name)

print("\nCourses:")
for course in students.values():
    print(course)

check_student = input("\nEnter student name to check: ")

if check_student in students:
    print("Student exists")
else:
    print("Student does not exist")
