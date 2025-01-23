from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    publicationYear: int
    genre: str

    author_id: int = Field(foreign_key="author.id")

    author: "Author" = Relationship(back_populates="books")

class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    nationality: str

    books: List[Book] = Relationship(back_populates="author")


# from typing import List, Optional
# from sqlmodel import Field, Relationship, SQLModel

# class Book(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     title: str
#     content: str
#     author_id: int = Field(foreign_key="author.id")

#     author: "Author" = Relationship(back_populates="books")

# class Author(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     email: str

#     books: List[Book] = Relationship(back_populates="author")