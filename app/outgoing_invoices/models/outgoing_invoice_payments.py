# It's a class that represents a payment made on an outgoing invoice
from datetime import datetime
from app.db import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey


class OutgoingInvoicePayment(Base):
    __tablename__ = "outgoing_invoices_payments"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    outgoing_invoice_payment_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_date = Column(Date, nullable=False)
    payment_description = Column(String(500))
    payment = Column(Float, nullable=False)

    outgoing_invoice_id = Column(Integer, ForeignKey("outgoing_invoices.outgoing_invoice_id"), nullable=False)

    def __init__(self, payment_date, payment_description, payment, outgoing_invoice_id):
        self.payment_date = datetime.strptime(payment_date, "%Y-%m-%d")
        self.payment_description = payment_description
        self.payment = payment
        self.outgoing_invoice_id = outgoing_invoice_id
