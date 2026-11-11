class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


students = [
    Student("Anastasia", 18),
    Student("Ivan", 20),
    Student("Olena", 19),
    Student("Valeria", 17),
    Student("Jon", 21)
]

sorted_students = sorted(students, key=lambda student: student.age)

print("List of students by age:")

for student in sorted_students:
    print(student)