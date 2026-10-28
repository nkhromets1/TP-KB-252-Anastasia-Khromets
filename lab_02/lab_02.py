import csv
from sys import argv

list = []

def loadList(fileName):
    with open(fileName, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append({
                "name": row["name"],
                "phone": row["phone"],
                "email": row["email"],
                "group": row["group"]
            })

def saveList(fileName):
    with open(fileName, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + \
                      ", Phone is " + elem["phone"] + \
                      ", Email is " + elem["email"] + \
                      ", Group is " + elem["group"]
        print(strForPrint)

def addNewElement(name=None, phone=None, email=None, group=None):
    if name is None:
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        email = input("Please enter student email: ")
        group = input("Please enter student group: ")

    newItem = {
        "name": name,
        "phone": phone,
        "email": email,
        "group": group
    }

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    list.insert(insertPosition, newItem)
    print("New element has been added")

def deleteElement(name=None):
    if name is None:
        name = input("Please enter name to be deleted: ")

    for item in list:
        if name == item["name"]:
            list.remove(item)
            print("Element has been deleted")
            return True

    print("Element was not found")
    return False

def updateElement(name=None, newName=None, newPhone=None,
                  newEmail=None, newGroup=None):
    if name is None:
        name = input("Please enter name to be updated: ")

    for item in list:
        if name == item["name"]:
            if newName is None:
                newName = input("Please enter new student name: ")
                newPhone = input("Please enter new student phone: ")
                newEmail = input("Please enter new student email: ")
                newGroup = input("Please enter new student group: ")

            list.remove(item)
            addNewElement(newName, newPhone, newEmail, newGroup)
            print("Element has been updated")
            return True

    print("Element was not found")
    return False

def main():
    fileName = argv[1]
    loadList(fileName)

    while True:
        chouse = input(
            "Please specify the action "
            "[ C create, U update, D delete, P print, X exit ] "
        )

        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()

            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()

            case "D" | "d":
                print("Element will be deleted")
                deleteElement()

            case "P" | "p":
                print("List will be printed")
                printAllList()

            case "X" | "x":
                saveList(fileName)
                print("List has been saved")
                print("Exit")
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()