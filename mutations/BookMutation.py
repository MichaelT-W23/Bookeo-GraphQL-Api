from sqlmodel import Session
import strawberry
from graphql_types import BookType
from database.models import Book
from database.db import engine

@strawberry.type 
class BookMutation:

    @strawberry.mutation
    def create_book(self, title: str, content: str, author_id: int) -> BookType:
        with Session(engine) as session:
            new_book = Book(title=title, content=content, author_id=author_id)
            session.add(new_book)
            session.commit()
            session.refresh(new_book)
            return BookType(id=new_book.id, title=new_book.title, content=new_book.content)
        