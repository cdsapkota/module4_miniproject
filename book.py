class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    def get_details(self):
        availability = "Available" if self.__is_available else "Not Available"
        details = (
        f"\nTitle: {self.__title}\n"
        f"Author: {self.__author}\n"
        f"Genre: {self.__genre}\n"
        f"Publication Date: {self.__publication_date}\n"
        f"Availability: {availability}"
        )
        return details


    def get_title(self):
        return self.__title
