class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        print("Age:", self.__age)


p1 = Person()

p1.set_age(20)
p1.get_age()