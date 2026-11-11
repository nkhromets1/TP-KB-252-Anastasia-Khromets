students = [
    {"name": "Anastasia", "mark": 90},
    {"name": "Jon", "mark": 82},
    {"name": "Olena", "mark": 74},
    {"name": "Bob", "mark": 60},
    {"name": "Valeria", "mark": 88}
]

print("Sort by name:")

for student in sorted(students, key=lambda elem: elem["name"]):
    print(f"Name: {student['name']}, Mark: {student['mark']}")

print("\nSort by mark:")

for student in sorted(students, key=lambda elem: elem["mark"]):
    print(f"Name: {student['name']}, Mark: {student['mark']}")