# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance

# a subclass can inherit attributes and methods from one class or *multiple* classes

# goal of exercise: how to reduce the duplication?
# also make it easier to introduce new classes by introducing some inheritance and class
# hierarchy
# makes it easier to manage


# create new class Publication for most obvious cases first (title, price)
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


# create new class Periodical for period, publisher duplication
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):  # have it inherit
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        # no longer need self.title and self.price
        # self.title = title
        # self.price = price
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    pass

    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

    #     self.title = title
    #     self.price = price
    #     self.period = period  # different from book
    #     self.publisher = publisher  # different from book


class Newspaper(Periodical):  # like Magazine
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        # self.title = title
        # self.price = price
        # self.period = period
        # self.publisher = publisher


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
