class Animal:
    def animal(self):
        print("I am an Animal")

class Dog(Animal):
    def dog(self):
        print("I am a Dog")

class Cat(Animal):
    def cat(self):
        print("I am a Cat")

a = Dog()
a.animal()

b = Cat()
b.animal()