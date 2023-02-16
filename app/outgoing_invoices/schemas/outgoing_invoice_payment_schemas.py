from pydantic import BaseModel
from typing import Optional
from datetime import date


class OutgoingInvoicePaymentSchema(BaseModel):
    outgoing_invoice_payment_id: int
    payment_date: date
    payment_description: Optional[str]
    payment: float
    outgoing_invoice_id: int

    class Config:
        orm_mode = True


class OutgoingInvoicePaymentIN(BaseModel):
    payment_date: str
    payment_description: Optional[str]
    payment: float
    outgoing_invoice_id: int

    class Config:
        orm_mode = True


class OutgoingInvoicePaymentUpdate(BaseModel):
    payment_date: Optional[str]
    payment_description: Optional[str]
    payment: Optional[float]
    outgoing_invoice_id: Optional[int]

    class Config:
        orm_mode = True
