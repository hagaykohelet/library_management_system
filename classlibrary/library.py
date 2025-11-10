from zoneinfo import available_timezones

from classesbook.books import Book
from classuser.user import User


class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, new_book: Book):
        for book in self.list_of_books:
            if new_book.isbn == book.isbn:
                print("this book in library")
        self.list_of_books.append(new_book)

    def add_user(self, new_user: User):
        for user in self.list_of_users:
            if new_user.id == user.id:
                print("youre already exist")
        self.list_of_users.append(new_user)

    def find_book(self, book_isbn):
        for book in self.list_of_books:
            if book.isbn == book_isbn and book.is_available:
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
            print("your not a library subscriber")
        elif not book:
            print("this book not in our library")
        elif not book.is_available:
            print("this book already borrowed")
        else:
            user.borrowed_books.append(book_isbn)
            book.is_available = False

    def return_book(self, user_id, book_isbn):
        user = self.find_user(user_id)
        book = self.find_book(book_isbn)
        if not user:
            print("your not a library subscriber")
        elif not book:
            print("this book not from our library")
        elif book.is_available:
            print("this book not in your borrowed list")
        else:
            user.borrowed_books.remove(book_isbn)
            book.is_available = True

    def list_available_books(self):
        available_books = []
        for book in self.list_of_books:
            if book.is_available:
                available_books.append(book.title)
        return available_books

    def search_book(self,title):
        for book in self.list_of_books:
            if book.title == title:
                return book
        return None



