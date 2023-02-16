from app.db import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey
from datetime import datetime


class IncomingInvoice(Base):
    __tablename__ = "incoming_invoices"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    incoming_invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    reference_code_invoice = Column(String(50), nullable=False)
    number_invoice = Column(String(50), nullable=False)
    invoice_date = Column(Date, nullable=False)
    net = Column(Float)
    vat = Column(Float)
    gross = Column(Float)
    description_invoice = Column(String(500))

    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), nullable=False)
    cost_center_id = Column(Integer, ForeignKey("cost_centers.cost_center_id"), nullable=True)

    def __init__(self, reference_code_invoice, number_invoice, invoice_date, net, vat, gross, description_invoice,
                 supplier_id, cost_center_id):
        self.reference_code_invoice = reference_code_invoice
        self.number_invoice = number_invoice
        self.invoice_date = datetime.strptime(invoice_date, "%Y-%m-%d")
        self.net = net
        self.vat = vat
        self.gross = gross
        self.description_invoice = description_invoice
        self.supplier_id = supplier_id
        self.cost_center_id = cost_center_id


