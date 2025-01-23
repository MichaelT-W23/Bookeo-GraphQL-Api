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
    age: int
    nationality: str
    books: List[BookType]