class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class student(person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age)
        self.school = school
        self.grade = grade

    def student_info(self):
        self.info()
        print("School:", self.school)
        print("Grade:", self.grade)

obj = student("Jeon Jungkook", 27, "Seoul University", "A")
obj.student_info()
    