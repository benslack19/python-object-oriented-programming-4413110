# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute."

    # TODO: create instance methods
    def getprice(self):
        # since discount isn't set during init, we can't rely on it being present
        # need to test for the existence of the attribute _discount
        if hasattr(self, "_discount"):  # note attribute is in quotes
            return self.price - self.price * self._discount
        else:
            return self.price

    def setdiscount(self, amount):
        # the underscore is a hint that this attribute is considered internal to the class
        # not for public consumption (it's actually functional in C# or Java)
        # for python it's just a convention to let other programmers know
        # note that there's no return here. it returns None if trying to access
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print("b1.price: ", b1.price)
print("b1.getprice: ", b1.getprice())

# TODO: try setting the discount
print("b1.price: ", b1.price)
print("b1.getprice: ", b1.getprice())
print("b1.setdiscount: ", b1.setdiscount(0.25))
print("b1.price after applying discount: ", b1.price)  # this stays the same
print("b1.getprice after applying discount: ", b1.getprice())  # this is different


# TODO: properties with double underscores are hidden by the interpreter; don't want subclasses inadvertently overwriting the attribute
# print(b2.__secret)  # this will fail
# but python does this by adding an underscore and class at the beginning so it can be suberted
print(b2._Book__secret)
