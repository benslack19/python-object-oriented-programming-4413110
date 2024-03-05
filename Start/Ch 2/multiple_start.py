# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

# python allows inheriting from multiple classes which not every programming language can do
# it can be useful but can cause problems if not used carefully
# complexity is why it isn't super common but it's used in interfaces (next video)


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"


# class C(A, B):  # lists both to do multiple inheritance
class C(B, A):  # lists both to do multiple inheritance but the order matters!
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(
            self.prop1
        )  # it'll work as long as attributes are not named the same across classes
        print(self.prop2)
        # if there's a name collision, then it will take inheritance in order listed
        # it would start with class C, and if it's not defined there then look in the classes it inherits from left to right
        print(self.name)


c = C()
print(C.__mro__)  # get method resolution order, note capital C it's a class attribute
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)   # goes all the way up to built-in python object
c.showprops()
