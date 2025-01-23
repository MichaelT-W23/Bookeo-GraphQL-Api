from sqlmodel import Session
import strawberry
from graphql_types import AuthorType
from database.models import Author
from database.db import engine

@strawberry.type 
class AuthorMutation:
    
    @strawberry.mutation
    def create_author(self, name: str, age: int, nationality: str) -> AuthorType:
        with Session(engine) as session:
            new_author = Author(name=name, age=age, nationality=nationality)
            session.add(new_author)
            session.commit()
            session.refresh(new_author)

            return AuthorType(
                id=new_author.id, 
                name=new_author.name, 
                age=new_author.age,
                nationality=new_author.nationality,
                books=[]
            )
        