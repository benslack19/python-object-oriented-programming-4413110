# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

# Magic methods
# set of methods that python automatically associates with every class definition
# customize object behavior and act like built-in python classes
# many methods but only covers most common
# Examples:
# define how objects are represented in strings
    # to the user and for debugging purposes
# control access to attribute values both for get and set
# build in comparison and equality testing capabilities
# allow objects to be called like functions; make it more concise and readable

# __str__ overwrite is typically used to have a user-friendly string
# __repr__ is more about an object representation


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"The book {self.title} by {self.author} costs {self.price}"

    # TODO: use the __repr__ method to return an obj representation
    def __repr__(self):
        # this can work but will fail eval
        # return f"title={self.title}, author={self.author}, price={self.price}"
        
        # for eval to work, it has to be the same format and same parameter order
        return f"Book('{self.title}', '{self.author}', '{self.price}')" 
    


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print("Both objects alone")
print("using print", b1)
print(b2)

# can do before or after editing magic method
# print(f"str for b1 before overwrite: {str(b1)}")
# print(f"repr for b1 before overwrite: {repr(b1)}")
# these give the same value

print(f"str for b1 after overwrite: {str(b1)}")

# this is more assigned to the class description but the main purpose is for developer debugging
print(f"repr for b1 after overwrite: {repr(b1)}")

# Using eval to identify the difference? (this is just me looking around)

# Get the repr representation of the object
b1_str = str(b1)
b1_repr = repr(b1)

# Use eval() to recreate the object
#recreated_b1_str = eval(b1_str)
recreated_b1_repr = eval(b1_repr)
#recreated_b1_repr = eval(repr(b1))


print("---STR----")
print("b1_str: ", b1_str)
print("b1_str type: ", type(b1_str))

print("---REPR----")
print("b1_repr: ", b1_repr)
print("b1_repr type: ", type(b1_repr))
print("recreated b1_repr: ", recreated_b1_repr)
print("recreated b1_repr type: ", type(recreated_b1_repr))


# list of magic methods
# https://rszalski.github.io/magicmethods/
