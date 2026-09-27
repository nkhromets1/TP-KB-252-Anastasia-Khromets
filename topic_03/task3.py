student = {
    "name": "Anastasia",
    "age": 18,
    "group": "KB-252"
}

print("Initial dictionary:", student)

student.update({"city": "Chernihiv"})
print("After update:", student)

del student["age"]
print("After del:", student)

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

student.clear()
print("After clear:", student)