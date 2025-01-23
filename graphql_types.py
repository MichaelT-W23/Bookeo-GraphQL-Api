from typing import List
import strawberry

@strawberry.type
class BookType:
    id: int
    title: str
    content: str

@strawberry.type
class AuthorType:
    id: int
    name: str
    email: str
    books: List[BookType]