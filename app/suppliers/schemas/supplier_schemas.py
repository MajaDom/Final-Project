from pydantic import BaseModel
from typing import Optional


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
