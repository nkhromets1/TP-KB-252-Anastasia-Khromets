from Student import Student
from StudentList import StudentList
from Utils import Utils

def test_add():
    studentList = StudentList()

    studentList.add_student("Bob", "111", "bob@gmail.com", "KB-251")

    assert len(studentList.students) == 1
    assert studentList.students[0].name == "Bob"


def test_delete():
    studentList = StudentList()

    studentList.add_student("Bob", "111", "bob@gmail.com", "KB-251")

    result = studentList.delete_student("Bob")

    assert result == True
    assert len(studentList.students) == 0


def test_update():
    studentList = StudentList()

    studentList.add_student("Bob", "111", "bob@gmail.com", "KB-251")

    result = studentList.update_student(
        "Bob", "Anna", "222", "anna@gmail.com", "KB-252"
    )

    assert result == True
    assert len(studentList.students) == 1
    assert studentList.students[0].name == "Anna"


def test_save_load(tmp_path):
    studentList = StudentList()

    studentList.add_student("Bob", "111", "bob@gmail.com", "KB-251")

    fileName = tmp_path / "test.csv"

    Utils.save_students(fileName, studentList.students)

    students = Utils.load_students(fileName)

    assert len(students) == 1
    assert students[0].name == "Bob"