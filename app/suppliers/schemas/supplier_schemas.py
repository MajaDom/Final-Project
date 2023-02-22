# SupplierSchema is the class that will be used to serialize the data from the database
from typing import Optional
from pydantic import BaseModel


class SupplierSchema(BaseModel):
    supplier_id: int
    supplier_name: str
    contact: str
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class SupplierSchemaIN(BaseModel):
    supplier_name: Optional[str]
    contact: Optional[str]

    class Config:
        orm_mode = True


class SupplierSchemaUpdate(BaseModel):
    supplier_name: Optional[str]
    contact: Optional[str]

    class Config:
        orm_mode = True
