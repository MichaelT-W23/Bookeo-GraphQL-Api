from fastapi import HTTPException
from sqlmodel import Session
import strawberry
from graphql_types import AuthorType
from database.models import Author
from database.db import engine

@strawberry.type
class AuthorQuery:
    
    @strawberry.field
    def get_author(self, id: int) -> AuthorType:
        with Session(engine) as session:
            author = session.get(Author, id)

            if not author:
                raise HTTPException(status_code=404, detail="Author not found")
            
            return AuthorType(
                id=author.id, 
                name=author.name, 
                age=author.age,
                nationality=author.nationality,
                books=[]
            )
            