class Father:
    def father(self):
        print("I'm Father")

class Mother:
    def mother(self):
        print("I'm Mother")

class Child:
    def child(self):
        print("I'm Child")

class GrandChild(Father, Mother, Child):
    def grandchild(self):
        print("I'm GrandChild")

obj = GrandChild()
obj.father()
obj.mother()
obj.child()
obj.grandchild()


