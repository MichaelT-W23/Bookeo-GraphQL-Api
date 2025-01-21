from sqlmodel import Session
import strawberry
from graphql_types import UserType
from database.models import User
from database.db import engine

@strawberry.type 
class UserMutation:
    
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> UserType:
        with Session(engine) as session:
            new_user = User(name=name, email=email)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return UserType(id=new_user.id, name=new_user.name, email=new_user.email, posts=[])
        