# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes
# it's just like doing it with init method

# field function provides flexibilty for default values
# it allows us to specify a function that will be called to provide the default value
from dataclasses import dataclass, field
import random

# attributes without default values need to come first
def price_func():
    return float(random.randrange(20, 40))

def price_func2(title):
    return float(len(title))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    #price: float = field(default_factory=lambda: price_func2(title))
    price: float = field(default_factory=price_func)


# b1 = Book()
# print(b1)

b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b2)
print(b3)