class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def get_details(self):
        borrowed_books = ', '.join(self.__borrowed_books) if self.__borrowed_books else "None"
        details = (
        f"\nName: {self.__name}\n"
        f"Library ID: {self.__library_id}\n"
        f"Borrowed Books: {borrowed_books}"
        )
        return details
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__library_id
