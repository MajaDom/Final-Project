from typing import Optional
from datetime import date
from pydantic import BaseModel


class AssignedEquipmentSchema(BaseModel):
    assigned_equipment_id: int
    start_date: date
    end_date: Optional[date]
    id_employee: int
    equipment_id: int

    class Config:
        orm_mode = True


class AssignedEquipmentSchemaIN(BaseModel):
    start_date: str
    end_date: Optional[str]
    id_employee: int
    equipment_id: int

    class Config:
        orm_mode = True


class AssignedEquipmentSchemaUpdate(BaseModel):
    start_date: Optional[str]
    end_date: Optional[str]
    id_employee: Optional[int]
    equipment_id: Optional[int]

    class Config:
        orm_mode = True
