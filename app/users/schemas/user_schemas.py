
from pydantic import BaseModel
from pydantic import UUID4, EmailStr
from pydantic.typing import Optional


class UserSchema(BaseModel):
    user_id: UUID4
    user_name: str
    email: str
    is_admin: bool
    is_active: bool

    class Config:
        orm_mode = True


class UserSchemaIN(BaseModel):
    user_name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaUpdate(BaseModel):
    user_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        orm_mode = True


class UserSchemaLogin(BaseModel):
    user_name: str
    password: str

    class Config:
        orm_mode = True
