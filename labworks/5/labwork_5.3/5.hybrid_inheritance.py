class A:
    def a(self):
        print("Method a from class A")
class B(A):
    def b(self):
        print("Method b from class B")

class C(A):
    def c(self):
        print("Method c from class C")

class D(B, C):
    def d(self):
        print("Method d from class D")

obj = D()
obj.a()
obj.b()
obj.c()
obj.d()




