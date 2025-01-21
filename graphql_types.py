from typing import List
import strawberry

@strawberry.type
class PostType:
    id: int
    title: str
    content: str

@strawberry.type
class UserType:
    id: int
    name: str
    email: str
    posts: List[PostType]