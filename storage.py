import json
import os

from classesbook.books import Book
from classuser.user import User

DATA_FILE = os.path.join("data", "library_data.json")
BOOKS_CSV = os.path.join("data", "books.csv")
USERS_CSV = os.path.join("data", "users.csv")


def ensure_data_dir():
    os.makedirs("data", exist_ok=True)


def save_data(books, users):
    ensure_data_dir()
    payload = {
        "books": [b.to_dict() for b in books],
        "users": [u.to_dict() for u in users]
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def load_data():
    ensure_data_dir()
    if not os.path.exists(DATA_FILE):
        return [], []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        payload = json.load(f)
    books = [Book.from_dict(d) for d in payload.get("books", [])]
    users = [User.from_dict(d) for d in payload.get("users", [])]
    return books, users
