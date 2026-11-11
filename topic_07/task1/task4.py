class Group:
    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

group = Group(["Anastasia", "Anna", "Olena"])

print(len(group))