# IncomingInvoiceSchema is a class that inherits from BaseModel and has the following attributes: incoming_invoice_id,
# reference_code_invoice, number_invoice, invoice_date, net, vat, gross, description_invoice, supplier_id, cost_center_id
from typing import Optional
from datetime import date
from pydantic import BaseModel


class IncomingInvoiceSchema(BaseModel):
    incoming_invoice_id: int
    reference_code_invoice: str
    number_invoice: str
    invoice_date: date
    net: Optional[float]
    vat: Optional[float]
    gross: Optional[float]
    description_invoice: Optional[str]
    supplier_id: int
    cost_center_id: Optional[int]

    class Config:
        orm_mode = True


class IncomingInvoiceSchemaIN(BaseModel):
    reference_code_invoice: str
    number_invoice: str
    invoice_date: str
    net: Optional[float]
    vat: Optional[float]
    gross: Optional[float]
    description_invoice: Optional[str]
    supplier_id: int
    cost_center_id: Optional[int]

    class Config:
        orm_mode = True


class IncomingInvoiceSchemaUpdate(BaseModel):
    reference_code_invoice: Optional[str]
    number_invoice: Optional[str]
    invoice_date: Optional[str]
    net: Optional[float]
    vat: Optional[float]
    gross: Optional[float]
    description_invoice: Optional[str]
    supplier_id: Optional[int]
    cost_center_id: Optional[int]

    class Config:
        orm_mode = True
