from fastapi import HTTPException
from sqlmodel import Session, select
import strawberry
from graphql_types import BookType
from database.models import Book
from database.db import engine

@strawberry.type
class BookQuery:

    @strawberry.field
    def get_all_books(self) -> list[BookType]:
        with Session(engine) as session:
            statement = select(Book)
            results = session.exec(statement).all()

            return [
                BookType(
                    id=book.id,
                    title=book.title,
                    publicationYear=book.publicationYear,
                    genre=book.genre,
                    author_id=book.author_id
                )
                for book in results
            ]
    
    @strawberry.field
    def get_book(self, id: int) -> BookType:
        with Session(engine) as session:
            book = session.get(Book, id)

            if not book:
                raise HTTPException(status_code=404, detail='Book not found')
            
            return BookType(
                id=book.id, 
                title=book.title, 
                publicationYear=book.publicationYear,
                genre=book.genre, 
                author_id=book.author_id
            )