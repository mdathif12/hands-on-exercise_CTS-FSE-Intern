from pydantic import BaseModel
from pydantic import EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int

    class Config:
        from_attributes = True