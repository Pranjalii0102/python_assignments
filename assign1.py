class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.isborrowed=False

    def borrow(self):
        if not self.isborrowed:
            self.isborrowed=True
            print(f"{self.title} has been borrowed ")
        else:
            print(f"{self.book} is not available cause it is altready borrowed")

    def return_book(self):
        if self.isborrowed:
            self.isborrowed=False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was not borrowed.")

    

class Patron:
    def __init__(self, name, patron_id):
        self.name=name
        self.patron_id=patron_id
        self.borrowed_books=[]

    def borrow_book(self,book):
        if not book.isborrowed:
            book.borrow()
            self.borrowed_books.append(book)

        else:    
            print(f"{book.tilte} is unavailable")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)

        else:    
            print(f"{book.tilte} was not borrowed by {self.name}")



class Library:
    def __init__(self):
        self.books=[]
        self.patrons=[]

    def add_books(self, book):
        self.books.append(book)
        print(f"Book {book.title} is added")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron {patron.name} is registered")

    def borrow_book(self, patron, book):
        patron.borrow_book(book)

    def return_book(self, patron, book):
        patron.return_book(book)


library=Library()

book1=Book("xyz", "XYZ",101)
book2=Book("abc", "ABC",102)
book3=Book("pqr", "PQR",103)

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

patron1=Patron("Aaditi", "p001")
patron2=Patron("Pranjalii", "p002")            
patron3=Patron("Pratiksha", "p003")

library.register_patron(patron1)
library.register_patron(patron2)
library.register_patron(patron3)

library.borrow_book(patron1, book1)
library.borrow_book(patron2, book2)
library.borrow_book(patron3, book3)

library.return_book(patron1, book1)
library.return_book(patron2, book2)
library.return_book(patron3, book3)