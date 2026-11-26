class Grandparent:
    def grandparent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def parent(self):
        print("I am Parent")

class Child(Parent):
    def child(self):
        print("I am Child")

c = Child()
c.grandparent()
c.parent()
c.child()