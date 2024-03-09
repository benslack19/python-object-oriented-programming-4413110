# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

# create complex objects our of simpler ones
# inheritance is an "is" relationship (book is a publication)
# composition is more of a "has" relationship (book object has an author object
# which contains information about the author, rather than defining everything under book class)

# inheritance and composition aren't mutually exclusive

# original Book class has author and chapter information
# let's separate it out instead


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # give this class a nice string representation
    # override built-in str representation
    # why is the overide needed?
    def __str__(self):
        return f"{self.fname} {self.lname}"

    # then modify Book class that takes Author as an argument and defaults to return None


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author  # refer to author object instead

        self.chapters = []

    # don't need to add chapter as a parameter in the constructor because it's only used in this method
    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print("auth: ", auth)
print("b1.title: ", b1.title)
print("b1.author: ", b1.author)
print("b1.getbookpagecount: ", b1.getbookpagecount())
