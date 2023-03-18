# The ClientContractSchema class is a Pydantic model that defines the schema of the ClientContract table
from typing import Optional, Literal
from datetime import date
from pydantic import BaseModel


class ClientContractSchema(BaseModel):
    client_contract_id: int
    contract_code: str
    start_date: date
    contract_description: Optional[str]
    end_date: Optional[date]
    client_id: int

    class Config:
        orm_mode = True


# A class that defines the schema of the data that will be passed into the function.
class ClientContractSchemaIN(BaseModel):
    contract_code: str
    start_date: str
    contract_description: Optional[str]
    end_date: Optional[str]
    client_id: int

    class Config:
        orm_mode = True


# > This class is used to update a client contract
class ClientContractSchemaUpdate(BaseModel):
    contract_code: Optional[str]
    start_date: Optional[str]
    contract_description: Optional[str]
    end_date: Optional[str]
    client_id: Optional[int]

    class Config:
        orm_mode = True
