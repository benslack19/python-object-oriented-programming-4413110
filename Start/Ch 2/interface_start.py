# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

# be able to use abstract base classes and multiple inheritance to implement
# a programming feature called an interface
# C# and Java provide this as a built-in part of the language but not python
# here's a workaround
# a particular makes a promise (contract) to provide a certain kind of capability

# suppose we wanted shape objects to be able to provide ability to represent
# themselves as json
# can make part of GraphicShape base class, but if we wanted other objects like that
# then we're duplicating code
# instead create another ABC called JSONify


from abc import ABC, abstractmethod


class JSONify(ABC):
    @abstractmethod  # just add a single abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(
    GraphicShape, JSONify
):  # add to inheritance list; it has effect of requiring override of toJSON abstract method
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius**2)

    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
