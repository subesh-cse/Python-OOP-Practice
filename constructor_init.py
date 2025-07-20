# constructor_init.py
# Demonstration of the __init__() constructor with default parameters

class Book:
    def __init__(self, title, author="Unknown", pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

# Create objects with and without optional parameters
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Python Crash Course")
book3 = Book("The Alchemist", pages=208)

book1.summary()
book2.summary()
book3.summary()
