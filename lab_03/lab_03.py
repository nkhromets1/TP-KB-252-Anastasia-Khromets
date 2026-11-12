from sys import argv
from StudentList import StudentList
from Utils import Utils

def main():
    fileName = argv[1]

    studentList = StudentList()

    studentList.students = Utils.load_students(fileName)

    while True:
        choice = input(
            "Please specify the action "
            "[ C create, U update, D delete, P print, X exit ] "
        )

        match choice:
            case "C" | "c":
                print("New element will be created:")

                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter student email: ")
                group = input("Please enter student group: ")

                studentList.add_student(name, phone, email, group)
                studentList.print_all()

            case "U" | "u":
                print("Existing element will be updated")

                name = input("Please enter name to be updated: ")
                newName = input("Please enter new student name: ")
                newPhone = input("Please enter new student phone: ")
                newEmail = input("Please enter new student email: ")
                newGroup = input("Please enter new student group: ")

                studentList.update_student(
                    name, newName, newPhone, newEmail, newGroup
                )

                studentList.print_all()

            case "D" | "d":
                print("Element will be deleted")

                name = input("Please enter name to be deleted: ")
                studentList.delete_student(name)

            case "P" | "p":
                print("List will be printed")
                studentList.print_all()

            case "X" | "x":
                Utils.save_students(fileName, studentList.students)

                print("List has been saved")
                print("Exit")
                break

            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()