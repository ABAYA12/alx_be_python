class Book:
    """A class to represent a book in the library."""
    def __init__(self, title, author):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class to manage a collection of books in the library."""
    def __init__(self):
        """Initialize a Library instance with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """
        Add a new book to the library collection.

        Args:
            book (Book): The book to be added.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book from the library by its title.

        Args:
            title (str): The title of the book to check out.

        Returns:
            str: A message indicating the result of the checkout process.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out."
                return f"'{title}' is already checked out."
        return f"'{title}' is not in the library."

    def return_book(self, title):
        """
        Return a book to the library by its title.

        Args:
            title (str): The title of the book to return.

        Returns:
            str: A message indicating the result of the return process.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' has been returned."
                return f"'{title}' was not checked out."
        return f"'{title}' is not in the library."

    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
