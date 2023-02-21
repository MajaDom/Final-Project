from typing import Optional
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


class ClientContractSchemaIN(BaseModel):
    contract_code: str
    start_date: str
    contract_description: Optional[str]
    end_date: Optional[str]
    client_id: int

    class Config:
        orm_mode = True


class ClientContractSchemaUpdate(BaseModel):
    contract_code: Optional[str]
    start_date: Optional[str]
    contract_description: Optional[str]
    end_date: Optional[str]
    client_id: Optional[int]

    class Config:
        orm_mode = True
