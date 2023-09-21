class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
students = [
    Student("Alice", "S001", 3.7),
    Student("Bob", "S002", 3.5),
    Student("Charlie", "S003", 4.0),
    Student("David", "S004", 3.9),
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")