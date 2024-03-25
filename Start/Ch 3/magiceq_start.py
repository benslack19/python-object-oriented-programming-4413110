# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

# objects don't know how to compare themselves to other objects
# we can use magic methods to define custom comparison logic
# we can also use them to define custom logic for math operations


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    # we're using value here to represent another instance of the class
    def __eq__(self, value):
        # exception handling to verify it's the same class
        if not isinstance(value, Book):
            raise ValueError("Can't compare to a non-Book object")

        return (
            self.title == value.title
            and self.author == value.author
            and self.price == value.price
        )

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare to a non-Book object")
        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare to a non-Book object")
        return self.price < value.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
# this will be False without the __eq__ method
# python's not checking the attributes
# it just sees that they are different objects in memory
print(b1 == b3)
# true once a proper __eq__ method is in place

print(b1 == b2)

# print(b1 == 19)  # raise ValueError

# TODO: Check for greater and lesser value
print("test for greater than", b1 > b2)
print("test for less than", b1 < b2)

# TODO: Now we can sort them too
books = [b1, b3, b2, b4]
books.sort()
print([book.title for book in books])
