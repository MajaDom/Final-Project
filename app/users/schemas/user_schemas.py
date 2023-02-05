from pydantic import BaseModel
from pydantic import UUID4, EmailStr


class UserSchema(BaseModel):
    user_id: UUID4
    user_name: str
    email: str
    password: str
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
