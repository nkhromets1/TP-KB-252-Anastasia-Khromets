list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-251"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "group": "KB-252"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@gmail.com", "group": "KB-241"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@gmail.com", "group": "KB-242"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + \
                      ", Phone is " + elem["phone"] + \
                      ", Email is " + elem["email"] + \
                      ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
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
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print("Element has been deleted")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
    else:
        del list[updatePosition]
        newName = input("Please enter new student name: ")
        newPhone = input("Please enter new student phone: ")
        newEmail = input("Please enter new student email: ")
        newGroup = input("Please enter new student group: ")
        newItem = {
            "name": newName,
            "phone": newPhone,
            "email": newEmail,
            "group": newGroup
        }
        insertPosition = 0
        for item in list:
            if newName > item["name"]:
                insertPosition += 1
            else:
                break
        list.insert(insertPosition, newItem)
        print("Element has been updated")
    return


def main():
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
                print("Exit")
                break
            case _:
                print("Wrong choice")


main()