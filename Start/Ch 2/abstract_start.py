# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

# fairly common design pattern:
# make a base class as a template for other classes to inherit from but with a twist:
# don't want consumers to use base class itself because it's just a blueprint
# also enforce the constraint that some methods and attributes from the base class
# must be implemented -> this is usefulness of abstract base classes

# working example: building a drawing program where user can create different
# kinds of shapes, want program to be extensible

# GraphicShape is the base class, want calcArea be used, prevent GraphicShape itself
# from bing implemented

from abc import ABC, abstractmethod  # abstract base class library


class GraphicShape(
    ABC
):  # add ABC here but g = GraphicShape() won't fail unless you add @abstractmethod decorator
    def __init__(self):
        super().__init__()

    # add decorator here. indicates no implementation in base class and each subclass has to override this method
    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius**2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side**2


# g = GraphicShape()  # will fail after

c = Circle(10)
print(c.calcArea())  # fails after adding decorator in ABC
s = Square(12)
print(s.calcArea())
