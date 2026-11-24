class Student:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


s1 = Student()
s2 = Student()
s3 = Student()

del s1
del s2
del s3