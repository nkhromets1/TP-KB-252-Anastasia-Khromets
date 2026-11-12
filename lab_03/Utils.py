import csv
from Student import Student

class Utils:
    @staticmethod
    def load_students(fileName):
        students = []

        with open(fileName, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["name"],
                    row["phone"],
                    row["email"],
                    row["group"]
                )

                students.append(student)

        students.sort(key=lambda student: student.name)

        return students

    @staticmethod
    def save_students(fileName, students):
        with open(fileName, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email", "group"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in students:
                writer.writerow({
                    "name": student.name,
                    "phone": student.phone,
                    "email": student.email,
                    "group": student.group
                })