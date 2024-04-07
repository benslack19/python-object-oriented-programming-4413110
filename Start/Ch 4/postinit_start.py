# Python Object Oriented Programming by Joe Marini course example
# Using the postinit function in data classes

# how to perform additional object initialization while using dataclass
# example: create attributes on book class that depends on values of other attributes
# __post_init__ is a special method that is called by the dataclass after the object has been initialized
# the learning exercise here is to create a description attribute that depends on the values of other attributes

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        # Anything under this block is a new attribute now
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


# create some Book objects
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: use the description attribute
print(b1.description)
print(b2.description)
