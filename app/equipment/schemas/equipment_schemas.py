# The EquipmentSchema class is a pydantic model that defines the schema of the equipment table in the database
from typing import Optional
from datetime import date
from pydantic import BaseModel


class EquipmentSchema(BaseModel):
    equipment_id: int
    invoice_code: str
    name: str
    category: str
    serial_number: str
    net: float
    vat: float
    date_of_purchase: date
    date_of_transaction: Optional[date]
    shop_name: str

    class Config:
        orm_mode = True


class EquipmentSchemaSchemaIN(BaseModel):
    invoice_code: str
    name: str
    category: str
    serial_number: str
    net: float
    vat: float
    date_of_purchase: str
    date_of_transaction: Optional[str]
    shop_name: str

    class Config:
        orm_mode = True


class EquipmentSchemaUpdate(BaseModel):
    invoice_code: Optional[str]
    name: Optional[str]
    category: Optional[str]
    serial_number: Optional[str]
    net: Optional[float]
    vat: Optional[float]
    date_of_purchase: Optional[str]
    date_of_transaction: Optional[str]
    shop_name: Optional[str]

    class Config:
        orm_mode = True
