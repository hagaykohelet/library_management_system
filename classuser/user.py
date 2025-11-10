from dataclasses import dataclass, asdict, field
from typing import List

@dataclass
class User:
    name: str
    id: str
    borrowed_books: List[str] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d):
        return User(
            name=d["name"],
            id=d["id"],
            borrowed_books=d.get("borrowed_books", [])
        )

    def __str__(self):
        return f"{self.name} (ID: {self.id}) - {len(self.borrowed_books)} borrowed"