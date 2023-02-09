from pydantic import BaseModel
from typing import Optional


class EmployeeSchema(BaseModel):
    id_employee: int
    first_name: str
    last_name: str
    contact: str
    user_id: Optional[str]

    class Config:
        orm_mode = True


class EmployeeSchemaIN(BaseModel):
    first_name: str
    last_name: str
    contact: str
    user_id: Optional[str]

    class Config:
        orm_mode = True


class EmployeeSchemaUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    contact: Optional[str]
    user_id: Optional[str]

    class Config:
        orm_mode = True
