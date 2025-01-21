from fastapi import HTTPException
from sqlmodel import Session
import strawberry
from graphql_types import UserType
from database.models import User
from database.db import engine

@strawberry.type
class UserQuery:
    
    @strawberry.field
    def get_user(self, id: int) -> UserType:
        with Session(engine) as session:
            user = session.get(User, id)

            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            
            return UserType(id=user.id, name=user.name, email=user.email, posts=user.posts)
            