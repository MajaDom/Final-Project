# The ClientSchema class is a Pydantic model that defines the data structure of the Client model
from typing import Optional
from pydantic import BaseModel


class ClientSchema(BaseModel):
    client_id: int
    client_name: str
    contact: str

    class Config:
        orm_mode = True


# > This class is used to validate the input data for the `/clients` endpoint
class ClientSchemaIN(BaseModel):
    client_name: str
    contact: str

    class Config:
        orm_mode = True


# > This class is used to update a client's information
class ClientSchemaUpdate(BaseModel):
    client_name: Optional[str]
    contact: Optional[str]

    class Config:
        orm_mode = True
