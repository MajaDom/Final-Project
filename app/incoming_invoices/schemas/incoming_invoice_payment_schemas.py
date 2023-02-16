from pydantic import BaseModel
from typing import Optional
from datetime import date


class IncomingInvoicePaymentSchema(BaseModel):
    incoming_invoice_payment_id: int
    payment_date: date
    payment_description: Optional[str]
    payment: float
    incoming_invoice_id: int

    class Config:
        orm_mode = True


class IncomingInvoicePaymentIN(BaseModel):
    payment_date: str
    payment_description: Optional[str]
    payment: float
    incoming_invoice_id: int

    class Config:
        orm_mode = True


class IncomingInvoicePaymentUpdate(BaseModel):
    payment_date: Optional[str]
    payment_description: Optional[str]
    payment: Optional[float]
    incoming_invoice_id: Optional[int]

    class Config:
        orm_mode = True
