class Book:
    def __init__(self,isbn, title, author, status='available', borrower=None ) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.status = status
        self.borrower = borrower

    def __str__(self) -> str:
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Status: {self.status}, Borrower: {self.borrower}"
    
    




class Library:
    def __init__(self) -> None:
        self.books = []

    
    def add_book(self, book_added):
        """ Add new book to the library.
            A book cannot be added if another book with the same ISBN already exists in the library.
        Args:
            isbn: The ISBN of the book
            title: The title of the book
            author: The author of the book
            status: The status of the book (available or borrowed)
            borrower: The name of the borrower

        Returns:
            None
        """
        ### YOUR CODE HERE 

        for bookI in self.books:
            if bookI.title == book_added.title :
                
                print("The book already exists in the library.")
                return
 
        self.books.append(book_added)
        print( f"{book_added.title} has been added to the library.")

    def borrow_book(self, isbn, borrower):
        """ Borrow a book from the library.
        Args:
            isbn: The ISBN of the book
            borrower: The name of the borrower
        Returns:
            None
        """
        ### YOUR CODE HERE
        for book in self.books:
            if book.isbn == isbn:
                if book.status=='available':
                    book.borrower = borrower
                    book.status = 'borrowed'
                    print(f"{book.title} has been borrowed by {borrower}.")
                    return
                else:
                    print(f"Book with ISBN: {book.isbn} is not available in the library.")
                    return
        else:
            print(f"Book with ISBN: {isbn} does not exist.")

    def return_book(self, isbn):
        """ Return a book to the library.

        Args:
            isbn: The ISBN of the book

        Returns:
            None
        """
        ### YOUR CODE HERE
        for book in self.books:
            if book.isbn == isbn:
                if book.borrower =='borrowed':
                    book.status = 'available'
                    book.borrower = None
                    print(f"Book with ISBN: {self.isbn} has been returned.")
                    return
                else:
                    print(f"{self.title} is not being borrowed.")
                    return
        else:
            print(f"Book with ISBN: {isbn} does not exist.")

    def list_books(self):
        """ List all books in the library

        Args:
            None

        Returns:
            None
        """
        ### YOUR CODE HERE
        for book in self.books:
            print(book)





### TEST:
if __name__=="__main__":
    # the Library Data Structure
    my_library = Library()

    my_library.add_book(Book(1111,"Python Programming", "Jon Doe"))
    my_library.add_book(Book(2222, "Learning AI", "Jane Smith"))
    my_library.borrow_book(1111, 'Ivan')
    my_library.borrow_book(1111, 'Stoyan')
    my_library.list_books()
    


### Expected output:
# Python Programming has been added to the library.
# Learning AI has been added to the library.
# Python Programming has been borrowed by Ivan
# Book with ISBN: 1111 is not available in the library.
# ISBN: 1111, Title: Python Programming, Author: Jon Doe, Status: borrowed, Borrower: Ivan
# ISBN: 2222, Title: Learning AI, Author: Jane Smith, Status: available, Borrower: None

