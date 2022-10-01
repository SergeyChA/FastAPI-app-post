from pydantic import BaseModel, EmailStr


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BasePost):
    pass


class Post(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
