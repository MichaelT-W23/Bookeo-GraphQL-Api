from fastapi import HTTPException
from sqlmodel import Session
import strawberry
from graphql_types import PostType
from database.models import Post
from database.db import engine

@strawberry.type
class PostQuery:
    
    @strawberry.field
    def get_post(self, id: int) -> PostType:
        with Session(engine) as session:
            post = session.get(Post, id)

            if not post:
                raise HTTPException(status_code=404, detail='Post not found')
            
            return PostType(id=post.id, title=post.title, content=post.content)
        
    