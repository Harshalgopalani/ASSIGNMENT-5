student_marks = {"harsh":45, "anita":38, "joe":35, "shilpa":55,}

name = input("Enter the student name to check marks: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the records.")

#Output:
# Enter the student name to check marks: anita
# anita's marks: 38

# Enter the student name to check marks: john
# Student 'john' not found in the records.