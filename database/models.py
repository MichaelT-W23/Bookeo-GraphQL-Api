from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    author_id: int = Field(foreign_key="user.id")

    author: "User" = Relationship(back_populates="posts")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

    posts: List[Post] = Relationship(back_populates="author")