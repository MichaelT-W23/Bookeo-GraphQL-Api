from sqlmodel import Session
import strawberry
from graphql_types import BookType
from database.models import Book
from database.db import engine

@strawberry.type 
class BookMutation:

    @strawberry.mutation
    def create_book(self, title: str, publicationYear: int, genre: str, author_id: int) -> BookType:
        with Session(engine) as session:
            new_book = Book(title=title, publicationYear=publicationYear, genre=genre, author_id=author_id)
            session.add(new_book)
            session.commit()
            session.refresh(new_book)
            return BookType(
                id=new_book.id, 
                title=new_book.title, 
                publicationYear=new_book.publicationYear,
                genre=new_book.genre, 
                author_id=new_book.author_id
            )
        