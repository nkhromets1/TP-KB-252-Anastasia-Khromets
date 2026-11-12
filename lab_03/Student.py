class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def display_info(self):
        return (
            "Student name is " + self.name +
            ", Phone is " + self.phone +
            ", Email is " + self.email +
            ", Group is " + self.group
        )