from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id:int
    username:str
    avatar:str
class PostCreate(BaseModel):
    user:User
    content:str
    image:Optional[str]=None
    likes:int
    commentsCount:int
    createdAt:datetime