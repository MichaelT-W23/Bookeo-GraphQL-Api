from sqlmodel import Session
import strawberry
from graphql_types import PostType
from database.models import Post
from database.db import engine

@strawberry.type 
class PostMutation:

    @strawberry.mutation
    def create_post(self, title: str, content: str, author_id: int) -> PostType:
        with Session(engine) as session:
            new_post = Post(title=title, content=content, author_id=author_id)
            session.add(new_post)
            session.commit()
            session.refresh(new_post)
            return PostType(id=new_post.id, title=new_post.title, content=new_post.content)
        