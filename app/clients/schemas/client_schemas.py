# The ClientSchema class is a Pydantic model that defines the data structure of the Client model
from typing import Optional, List
from pydantic import BaseModel
from .client_contracts_schemas import ClientContractSchema


class ClientSchema(BaseModel):
    """Class that is used in routes as a response model for clients."""
    client_id: int
    client_name: str
    contact: str
    client_contract: List[ClientContractSchema]

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
