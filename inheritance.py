
class A:
    def greet(self):
        print("Hello from A")
        print("A")
        print()

class B(A):
    def greet(self):
        print("Hello from B")
        print("B(A)")
        print()
        super().greet()

class C(A):
    def greet(self):
        print("Hello from C")
        print("C(A)")
        print()
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from D")
        print("D(B,C)")
        print()
        super().greet()

a = input("type your name: ")
b = input("type your age: ")


d = D()
print(D.__mro__)
d.greet()
print()
print(B.__mro__)
b = B()
b.greet()
