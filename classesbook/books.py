from dataclasses import dataclass, asdict

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    is_available: bool = True

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d):
        return Book(
            title=d["title"],
            author=d["author"],
            isbn=d["isbn"],
            is_available=d.get("is_available", True)
        )

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) [{status}]"