class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Returns a user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation for object recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

