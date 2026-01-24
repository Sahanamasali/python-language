class Parent:
    def _init_(self):
        print("Parent constructor")

class Child(Parent):
    def _init_(self):
        super()._init_()
        print("Child constructor")

obj = Child()
