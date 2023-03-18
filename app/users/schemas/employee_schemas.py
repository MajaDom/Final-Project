# EmployeeSchema is the class that will be used to serialize the data from the database
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from .employment_contract_schema import EmploymentContractSchema


class EmployeeSchema(BaseModel):
    id_employee: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    user_id: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True


class EmployeeSchemaWithContracts(BaseModel):
    id_employee: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    user_id: Optional[str]
    is_active: bool
    contracts: List[EmploymentContractSchema]

    class Config:
        orm_mode = True


class EmployeeSchemaIN(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr]
    phone_number: str
    user_id: Optional[str]

    class Config:
        orm_mode = True


class EmployeeSchemaUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    user_id: Optional[str]

    class Config:
        orm_mode = True
