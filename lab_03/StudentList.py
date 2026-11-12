from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, name, phone, email, group):
        new_student = Student(name, phone, email, group)

        self.students.append(new_student)
        self.students.sort(key=lambda student: student.name)

        print("New element has been added")

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("Element has been deleted")
                return True

        print("Element was not found")
        return False

    def update_student(self, name, new_name, new_phone,
                       new_email, new_group):
        for student in self.students:
            if student.name == name:
                student.name = new_name
                student.phone = new_phone
                student.email = new_email
                student.group = new_group

                self.students.sort(key=lambda student: student.name)

                print("Element has been updated")
                return True

        print("Element was not found")
        return False

    def print_all(self):
        for student in self.students:
            print(student.display_info())