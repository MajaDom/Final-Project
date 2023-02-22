# IncomingInvoicePayment is a class that represents a payment made on an incoming invoice
from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey
from app.db import Base


class IncomingInvoicePayment(Base):
    __tablename__ = "incoming_invoices_payments"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    incoming_invoice_payment_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_date = Column(Date, nullable=False)
    payment_description = Column(String(500))
    payment = Column(Float, nullable=False)

    incoming_invoice_id = Column(Integer, ForeignKey("incoming_invoices.incoming_invoice_id"), nullable=False)

    def __init__(self, payment_date, payment_description, payment, incoming_invoice_id):
        self.payment_date = datetime.strptime(payment_date, "%Y-%m-%d")
        self.payment_description = payment_description
        self.payment = payment
        self.incoming_invoice_id = incoming_invoice_id
