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

    def print_title(self):
        print(f"The title is {self.title}")


# create new class Periodical for period, publisher duplication
class Periodical(Publication):
    def __init__(self, title, period, publisher, price):

        super().__init__(title, price)
        # self.title = title + " periodical"
        title = title + " periodical"
        self.period = period
        self.publisher = publisher

    # def print_title(self, publisher):
    #     print(f"The title is {self.title}")


pub1 = Publication("NYtimes", 1.99)
per1 = Periodical("SI", "Monthly", "Time", 5.99)
print(pub1.title, pub1.price)
print(pub1.print_title())
print(per1.title, per1.period, per1.publisher, per1.price)
per1.print_title()


# p2 = Periodical_no_price("SI", 3.40, "Monthly", "Time")


# what if you don't use all attributes in super().__init__ and add others?
# class Periodical_no_price(Publication):
#     def __init__(self, title, period, publisher):
#         super().__init__(title)
#         self.period = period
#         self.publisher = publisher


class Book(Publication):  # have it inherit
    def __init__(self, title, price, author, pages):
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


# p1 = Periodical("SI", "Monthly", "Time", 5.99)

# # p2 = Periodical_no_price("SI", 3.40, "Monthly", "Time")
# b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
# n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
# m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

# print(p1.title, p1.period, p1.publisher, p1.price)
# # print("printing title: ", p1.print_title("Time"))

# # print("Periodical no price: ", p2.title, p2.period, p2.publisher)
# print(b1.author)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)
