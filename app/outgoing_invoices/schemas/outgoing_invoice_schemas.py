from typing import Optional
from datetime import date
from pydantic import BaseModel


class OutgoingInvoiceSchema(BaseModel):
    outgoing_invoice_id: int
    reference_code_invoice: str
    start_date: date
    date_of_transaction: date
    net: Optional[float]
    vat: Optional[float]
    gross: Optional[float]
    description_invoice: Optional[str]
    status: Optional[bool]
    certified_invoice: str
    client_id: int
    cost_center_id: Optional[int]

    class Config:
        orm_mode = True


class OutgoingInvoiceSchemaIN(BaseModel):
    reference_code_invoice: str
    start_date: str
    date_of_transaction: str
    net: Optional[float]
    vat: Optional[float]
    gross: Optional[float]
    description_invoice: Optional[str]
    status: Optional[bool]
    certified_invoice: str
    client_id: int
    cost_center_id: Optional[int]

    class Config:
        orm_mode = True


class OutgoingInvoiceSchemaUpdate(BaseModel):
    reference_code_invoice: Optional[str]
    start_date: Optional[str]
    date_of_transaction: Optional[str]
    net: Optional[float]
    vat: Optional[float]
    gross: Optional[float]
    description_invoice: Optional[str]
    status: Optional[bool]
    certified_invoice: Optional[str]
    client_id: Optional[int]
    cost_center_id: Optional[int]

    class Config:
        orm_mode = True
