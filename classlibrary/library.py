from classesbook.books import Book
from classuser.user import User


class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, new_book: Book):
        for book in self.list_of_books:
            if new_book.isbn == book.isbn:
                print("this book in library\n")
                return
        self.list_of_books.append(new_book)
        print(f"book: {new_book.title} added to library\n")

    def add_user(self, new_user: User):
        for user in self.list_of_users:
            if new_user.id == user.id:
                print("youre already exist\n")
                return
        self.list_of_users.append(new_user)
        print(f"user: {new_user.name} added to library\n")

    def find_book(self, book_isbn):
        for book in self.list_of_books:
            if book.isbn == book_isbn:
                return book
        return None

    def find_user(self, user_id):
        for user in self.list_of_users:
            if user_id == user.id:
                return user
        return None

    def borrow_book(self, user_id, book_isbn):
        user = self.find_user(user_id)
        book = self.find_book(book_isbn)
        if not user:
            print("your not a library subscriber\n")
        elif not book:
            print("this book not in our library\n")
        elif not book.is_available:
            print("this book already borrowed\n")
        else:
            user.borrowed_books.append(book_isbn)
            book.is_available = False
            print("book borrowed successfully\n")
            return True

    def return_book(self, user_id, book_isbn):
        user = self.find_user(user_id)
        book = self.find_book(book_isbn)
        if not user:
            print("your not a library subscriber\n")
        elif not book:
            print("this book not from our library\n")
        elif book.is_available:
            print("this book not in your borrowed list\n")
        else:
            user.borrowed_books.remove(book_isbn)
            book.is_available = True
            print("book return successfully\n")
            return True

    def list_available_books(self):
        available_books = []
        for book in self.list_of_books:
            if book.is_available:
                available_books.append(book.title)
        return available_books

    def search_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                return book
        return None
