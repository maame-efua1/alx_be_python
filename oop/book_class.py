class Book:
    def __init__(self, title, author, year):
        """Constructor: initializes the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """String representation used by print() and str()."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: called when the object is deleted."""
        print(f"Deleting {self.title}")


if __name__ == "__main__":
    # Example run
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book
