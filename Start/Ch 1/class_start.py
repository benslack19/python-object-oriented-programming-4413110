# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods

# instance method: works on specific instances

# class method: shared at class level across all instances of class

# static method: they don't modify the state of either the class or the object instance
# not super common
# but it may make sense when you want method to belong to the class but don't need to access properties
# can implement in a singleton(?) design pattern
# singleton design pattern prevents you from making more than one instance of that class
# example: want book class to keep track of list of books


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    # example: create an attribute (book type) that applies to all instances of the class
    # use all caps to indicate it's a class attribute that applies to all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # edit init method below to make sure that booktype is one of the values that the class allows

    # TODO: double-underscore properties are hidden from other classes
    # used with static method in this example
    __booklist = None

    # TODO: create a class method
    # for class methods, instead of receiving object instance as first argument
    # the first argument is the class itself
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES  # this will simply return the list we created above

    # TODO: create a static method to expose __booklist property to consumers of the book class
    @staticmethod  # not put in course code
    def getbooklist():  # note no arguments
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist  # if it's been created return the list

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        # need to use `Book` to access BOOK_TYPES
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book types: ", Book.get_book_types())

# TODO: Create some book instances
b1 = Book("Title1", "HARDCOVER")
# b2 = Book("Title2", "COMIC")  # this will return a ValueError
b2 = Book("Title2", "PAPERBACK")  # this will return a ValueError

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()  # method of the class
thebooks.append(b1)
thebooks.append(b2)
print("thebooks singleton object: ", thebooks)

# explain singleton
print("Testing singleton")
thebooks2 = Book.getbooklist()  # method of the class
print(thebooks2)
print("are thebooks1 and thebooks2 equal? ", thebooks == thebooks2)
