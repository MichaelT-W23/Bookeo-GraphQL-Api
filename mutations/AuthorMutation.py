from sqlmodel import Session
import strawberry
from graphql_types import AuthorType
from database.models import Author
from database.db import engine

@strawberry.type 
class AuthorMutation:
    
    @strawberry.mutation
    def create_author(self, name: str, email: str) -> AuthorType:
        with Session(engine) as session:
            new_author = Author(name=name, email=email)
            session.add(new_author)
            session.commit()
            session.refresh(new_author)
            return AuthorType(id=new_author.id, name=new_author.name, email=new_author.email, books=[])
        