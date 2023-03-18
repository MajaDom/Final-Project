# It's a schema for the employment contract table
from datetime import date
from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime


class EmploymentContractSchema(BaseModel):
    id_row: int
    contract_type: str
    start_date: date
    end_date: Optional[date]
    paycheck: float
    is_active: bool
    termination_date: Optional[date]
    description_contract: Optional[str]
    fk_employee_id: int

    class Config:
        orm_mode = True


class EmploymentContractSchemaIn(BaseModel):
    contract_type: str
    start_date: str
    end_date: Optional[str]
    paycheck: float
    termination_date: Optional[str]
    description_contract: Optional[str]
    fk_employee_id: int

    @validator('termination_date', pre=True)
    def validate_termination_date(cls, value, values):
        if not value:
            return value  # Optional fields should return None if not provided
        try:
            try_date = datetime.strptime(value, '%Y-%m-%d')
            if 'start_date' in values and try_date < datetime.strptime(values['start_date'], '%Y-%m-%d'):
                raise ValueError('Termination_date must be after start_date')
        except ValueError:
            raise ValueError('invalid date format for termination_date')
        return value

    @validator('start_date', pre=True)
    def validate_start_date(cls, value, values):
        if not value:
            return value  # Optional fields should return None if not provided
        try:
            try_date = datetime.strptime(value, '%Y-%m-%d')
            if 'end_date' in values and try_date < datetime.strptime(values['end_date'], '%Y-%m-%d'):
                raise ValueError('start_date must be before end_date')
        except ValueError:
            raise ValueError('invalid date format for start_date')
        return value

    class Config:
        orm_mode = True


class EmploymentContractSchemaUpdate(BaseModel):

    contract_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    paycheck: Optional[float]
    start_date: Optional[str]
    end_date: Optional[str]
    termination_date: Optional[str]
    description_contract: Optional[str]

    class Config:
        orm_mode = True
