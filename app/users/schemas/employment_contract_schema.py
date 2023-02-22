# It's a schema for the employment contract table
from datetime import date
from typing import Optional
from pydantic import BaseModel


class EmploymentContractSchema(BaseModel):
    id_row: int
    start_date: date
    end_date: Optional[date]
    contract_type: str
    paycheck: float
    is_active: bool
    fk_employee_id: int

    class Config:
        orm_mode = True


class EmploymentContractSchemaIn(BaseModel):
    start_date: str
    end_date: Optional[str]
    contract_type: str
    paycheck: float
    fk_employee_id: int

    class Config:
        orm_mode = True


class EmploymentContractSchemaUpdate(BaseModel):
    start_date: Optional[str]
    end_date: Optional[str]
    contract_type: Optional[str]
    paycheck: Optional[float]

    class Config:
        orm_mode = True
