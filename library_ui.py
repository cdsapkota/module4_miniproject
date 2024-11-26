from book import Book
from user import User
from author import Author

class LibraryUI:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.book_menu()
            elif choice == '2':
                self.user_menu()
            elif choice == '3':
                self.author_menu()
            elif choice == '4':
                print("Thank you for using the Library Management System!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_menu(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                genre = input("Enter genre: ")
                pub_date = input("Enter publication date: ")
                self.books.append(Book(title, author, genre, pub_date))
                print(f"Book '{title}' added successfully.")
            elif choice == '2':
                title = input("Enter book title to borrow: ")
                book = next((b for b in self.books if b.get_title() == title), None)
                if not book:
                    print(f"Book '{title}' not found.")
                    continue

                if not book.borrow_book():
                    print(f"Book '{title}' is already borrowed.")
                    continue

                library_id = input("Enter your Library ID: ")
                user = next((u for u in self.users if u.get_id() == library_id), None)

                if not user:
                    print(f"User with ID '{library_id}' not found.")
                    name = input("Enter your name to register: ")
                    user = User(name, library_id)
                    self.users.append(user)
                    print(f"User '{name}' added successfully.")

                user.borrow_book(title)
                print(f"Book '{title}' borrowed successfully by {user.get_name()}.")
            elif choice == '3':
                title = input("Enter book title to return: ")
                book = next((b for b in self.books if b.get_title() == title), None)
                if not book:
                    print(f"Book '{title}' not found.")
                    continue

                library_id = input("Enter your Library ID: ")
                user = next((u for u in self.users if u.get_id() == library_id), None)

                if user and title in user.get_details():
                    book.return_book()
                    user.return_book(title)
                    print(f"Book '{title}' returned successfully.")
                else:
                    print(f"No record of user '{library_id}' borrowing this book.")
            elif choice == '4':
                title = input("Enter book title to search: ")
                book = next((b for b in self.books if b.get_title() == title), None)
                if book:
                    print(book.get_details())
                else:
                    print(f"Book '{title}' not found.")
            elif choice == '5':
                for book in self.books:
                    print(book.get_details())
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_menu(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter user name: ")
                library_id = input("Enter library ID: ")
                self.users.append(User(name, library_id))
                print(f"User '{name}' added successfully.")
            elif choice == '2':
                library_id = input("Enter library ID to view details: ")
                user = next((u for u in self.users if u.get_id() == library_id), None)
                if user:
                    print(user.get_details())
                else:
                    print(f"User with ID '{library_id}' not found.")
            elif choice == '3':
                for user in self.users:
                    print(user.get_details())
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def author_menu(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter author name: ")
                biography = input("Enter biography: ")
                self.authors.append(Author(name, biography))
                print(f"Author '{name}' added successfully.")
            elif choice == '2':
                name = input("Enter author name to view details: ")
                author = next((a for a in self.authors if a.get_details()['Name'] == name), None)
                if author:
                    print(author.get_details())
                else:
                    print(f"Author '{name}' not found.")
            elif choice == '3':
                for author in self.authors:
                    print(author.get_details())
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
