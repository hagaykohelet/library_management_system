import storage
from classesbook.books import Book
from classuser.user import User
from classlibrary.library import Library
from utils.utils import input_nonempty, export_to_csv
from storage import *


class PrintMenu:
    print("""
----Library system----
1.Add book
2.Add user
3.Borrow book
4.Return book
5.Show available books
6.Search book
7.Export csv
8.Save & exit 
""")


def main():
    book, user = storage.load_data()
    library = Library()
    while True:
        PrintMenu()
        choice = input_nonempty("Please enter your choice: ")

        if choice == "1":
            title = input("please enter a title of book ")
            author = input("please enter a author of book ")
            isbn = input("please enter a isbn of book ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)


        elif choice == "2":
            name = input("please enter your name ")
            id = input("please enter your id ")
            new_user = User(name, id)
            library.add_user(new_user)


        elif choice == "3":
            user_id = input("please enter your id ")
            to_borrow_book = input("please enter isbn of this book: ")
            library.borrow_book(user_id, to_borrow_book)

        elif choice == "4":
            user_id = input("please enter your id ")
            return_a_book = input("please enter isbn of this book: ")
            library.return_book(user_id, return_a_book)

        elif choice == "5":
            print(f"the available book is: {library.list_available_books()}\n")

        elif choice == "6":
            title_book = input("please enter a title of your book that you search: ")
            if library.search_book(title_book):
                print(f"{library.search_book(title_book)}\n")
            else:
                print(f"{title_book}\n")

        elif choice == "7":
            filename = input("enter filename for csv export ")
            export_to_csv(library.list_of_books, filename)
            print(f"data exported to {filename} successfully\n")

        elif choice == "8":
            storage.save_data(library.list_of_books, library.list_of_users)
            print("data saved exiting\n")
            print("good bye. ")
            break

        else:
            print("invalid input try again")


main()
