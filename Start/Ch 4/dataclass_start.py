# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

# seems like we can obviate __init__ and __repr__ methods

from dataclasses import dataclass

@dataclass
class Book:
    # def __init__(self, title, author, pages, price):
    #     self.title = title
    #     self.author = author
    #     self.pages = pages
    #     self.price = price
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title}, by {self.author}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)   # gives back a nice __repr__ method

# TODO: comparing two dataclasses - they implement __eq__
print(b1==b3)  # expect True
print(b1==b2)  # expect False

# TODO: change some fields
print(f"b1.bookinfo before change: {b1.bookinfo()}")
b1.title = "Beavis and Butthead"
b1.price = 69.99

print(f"b1.bookinfo after change: {b1.bookinfo()}")
