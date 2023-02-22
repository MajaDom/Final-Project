# The OutgoingInvoice class is a representation of the outgoing_invoices table in the database
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, Date, Float, ForeignKey
from app.db import Base


class OutgoingInvoice(Base):
    __tablename__ = "outgoing_invoices"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    outgoing_invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    reference_code_invoice = Column(String(50), nullable=False)
    start_date = Column(Date, nullable=False)
    date_of_transaction = Column(Date, nullable=False)
    net = Column(Float)
    vat = Column(Float)
    gross = Column(Float)
    description_invoice = Column(String(500))
    status = Column(Boolean, default=True)
    certified_invoice = Column(String(10))  # three possible values +,-,*

    client_id = Column(Integer, ForeignKey("clients.client_id"), nullable=False)
    cost_center_id = Column(Integer, ForeignKey("cost_centers.cost_center_id"), nullable=False)

    def __init__(self, reference_code_invoice, start_date, date_of_transaction, net, vat, gross, description_invoice,
                 certified_invoice, client_id, cost_center_id):
        self.reference_code_invoice = reference_code_invoice
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.date_of_transaction = datetime.strptime(date_of_transaction, "%Y-%m-%d")
        self.net = net
        self.vat = vat
        self.gross = gross
        self.description_invoice = description_invoice
        self.certified_invoice = certified_invoice
        self.client_id = client_id
        self.cost_center_id = cost_center_id
