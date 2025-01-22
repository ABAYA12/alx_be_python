class Book():
    # add a private attribute called is_checkout_
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__is_checkout = False

class Library():
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)
        print(f"Book '{book.__title}' added to the library.")

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            print(f"Book '{book.__title}' removed from the library.")
        else:
            print(f"Book '{book.__title}' not found in the library.")
            
    def checkout_book(self, book):
        if book in self.__books and not book.__is_checkout:
            book.__is_checkout = True
            print(f"Book '{book.__title}' checked out by {book.__author}.")
        else:
            print(f"Book '{book.__title}' is either already checked out or not found in the library.")

    def return_book(self, book):
        if book in self.__books and book.__is_checkout:
            book.__is_checkout = False
            print(f"Book '{book.__title}' returned by {book.__author}.")
        else:
            print(f"Book '{book.__title}' is either not checked out or not found in the library.")

    def display_books(self):
        print("Books in the library:")
        for book in self.__books:
            print(f"'{book.__title}' by {book.__author}{' (Checked Out)' if book.__is_checkout else ''}")

# def main():
#     # Create a library
#     library = Library()

#     # Create some books
#     book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
#     book2 = Book("To Kill a Mockingbird", "Harper Lee")
#     book3 = Book("1984", "George Orwell")

#     # Add books to the library
#     library.add_book(book1)
#     library.add_book(book2)
#     library.add_book(book3)

#     # Display the books in the library
#     library.display_books()

#     # Checkout a book
#     library.checkout_book(book1)
#     library.checkout_book(book2)
#     library.checkout_book(book3)

#     # Display the books in the library
#     library.display_books()

#     # Return a book
#     library.return_book(book1)

#     # Display the books in the library
#     library.display_books()

#     # Remove a book
#     library.remove_book(book2)

#     # Display the books in the library
#     library.display_books()