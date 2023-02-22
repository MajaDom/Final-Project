# IncomingInvoicePaymentSchema is the class that is used to return the data to the client.
# IncomingInvoicePaymentIN is the class that is used to receive the data from the client.
# IncomingInvoicePaymentUpdate is the class that is used to update the data in the database
from typing import Optional
from datetime import date
from pydantic import BaseModel


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
