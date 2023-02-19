from pydantic import BaseModel
from typing import Optional


class CostCenterSchema(BaseModel):
    cost_center_id: int
    center_name: str
    center_code: str

    class Config:
        orm_mode = True


class CostCenterSchemaIN(BaseModel):
    center_name: str
    center_code: str

    class Config:
        orm_mode = True


class CostCenterSchemaUpdate(BaseModel):
    center_code: Optional[str]
    center_name: Optional[str]

    class Config:
        orm_mode = True
