class Student():
    def __init__(self, name):
        self.name = name


students = []
s = Student("John")
students.append(s)
print(students[0].name)
print(students)
