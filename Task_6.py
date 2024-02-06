class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_students(self)

class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.students = []

    def add_students(self, student):
        self.students.append(student)