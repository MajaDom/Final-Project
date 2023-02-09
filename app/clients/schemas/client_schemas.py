from pydantic import BaseModel
from typing import Optional


class ClientSchema(BaseModel):
    client_id: int
    client_name: str
    contact: str

    class Config:
        orm_mode = True


class ClientSchemaIN(BaseModel):
    client_name: str
    contact: str

    class Config:
        orm_mode = True


class ClientSchemaUpdate(BaseModel):
    client_name: Optional[str]
    contact: Optional[str]

    class Config:
        orm_mode = True
