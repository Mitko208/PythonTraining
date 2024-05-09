def add_book(isbn, title, author, status='available', borrower=None):
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
    
    book = {'isbn':isbn, 'title':title, 'author':author, 'status':status, 'borrower':borrower }

    #Check if it already is in the library
    in_library = False
    
    for i in range(len(library)):
        if book['title'] == library[i]['title']:
            
            in_library= True
            break
    
    # Add if it isn't
    if in_library == True:
        print("The book already exists in the library.")
    else: 
        library.append(book)
        print( f"{book['title']} has been added to the library.")

    

def borrow_book(isbn, borrower):
    """ Borrow a book from the library.
    Args:
        isbn: The ISBN of the book
        borrower: The name of the borrower
    Returns:
        None
    """
    ### YOUR CODE HERE

    #if not any(book['isbn'] == isbn for book in library):
    #    print("does not exist in the library")                                     from Internet
    #    print(f"Book with ISBN: {isbn} is not available in the library.")

    #Check if the book exists
    book_exists = None
    for i in range(len(library)):                                                   #My solution
        if isbn == library[i]['isbn']:
            
            book_exists = True
            break
        else: 
            book_exists = False
        
    if book_exists == False:
        print(f"{isbn} does not exist in the library")
        
    else:
        for book in library:
            # Need to check it again to access the right dictionary 
            if book['isbn'] == isbn:

                if book['status']=='available':
                    book['borrower'] = borrower
                    book['status'] = 'borrowed'
                    print(f"{book['title']} has been borrowed by {borrower}.")
                    break

                elif book['status']=='borrowed':
                    print(f"Book with ISBN: {book['isbn']} is not available in the library.")
                    break






    

def return_book(isbn):
    """ Return a book to the library.

    Args:
        isbn: The ISBN of the book

    Returns:
        None
    """
    ### YOUR CODE HERE
    
    #Check if the book exists
    book_exists = None

    for i in range(len(library)):
        if isbn == library[i]['isbn']:
            
            book_exists = True
            break
        else: 
            book_exists = False
        
    if book_exists == False:
        print(f"{isbn} does not exist in the library")
    else:
        for book in library:
            # Need to check it again to access the right dictionary 
            if book['isbn'] == isbn:

                if book['status']=='borrowed':
                    book['status'] = 'available'
                    book['borrower'] = None
                    print(f"Book with ISBN: {book['isbn']} has been returned.")
                    break


def list_books():
    """ List all books in the library

    Args:
        None

    Returns:
        None
    """
    ### YOUR CODE HERE
    for i in range(len(library)):
        print("ISBN: ",library[i]['isbn'],", ","Title: ", library[i]['title'],", ","Author: ", library[i]['author'],", ",
               "Status: ",library[i]['status'],", ","Borrower: ", library[i]['borrower'],sep= "")
### TEST:
if __name__=="__main__":
    # the Library Data Structure
    library = []

    add_book(1111,"Python Programming", "Jon Doe")
    add_book(2222, "Learning AI", "Jane Smith")
    borrow_book(1111, 'Ivan')
    borrow_book(1111, 'Stoyan')
    list_books()
    


### Expected output:
# Python Programming has been added to the library.
# Learning AI has been added to the library.
# Python Programming has been borrowed by Ivan
# Book with ISBN: 1111 is not available in the library.
# ISBN: 1111, Title: Python Programming, Author: Jon Doe, Status: borrowed, Borrower: Ivan
# ISBN: 2222, Title: Learning AI, Author: Jane Smith, Status: available, Borrower: None

