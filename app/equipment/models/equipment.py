from app.db import Base
from sqlalchemy import Column, String, Integer, Date, Float
from datetime import datetime


class Equipment(Base):
    __tablename__ = "equipment"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    equipment_id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_code = Column(String(45), nullable=False)
    name = Column(String(200), nullable=False)
    category = Column(String(200), nullable=False)
    serial_number = Column(String(200), unique=True, nullable=False)
    net = Column(Float, nullable=False)
    vat = Column(Float, nullable=False)
    date_of_purchase = Column(Date, nullable=False)
    date_of_transaction = Column(Date, nullable=True)
    shop_name = Column(String(200), unique=True, nullable=False)

    def __init__(self, invoice_code, name, category, serial_number, net, vat, date_of_purchase, date_of_transaction,
                 shop_name):
        self.invoice_code = invoice_code
        self.name = name
        self.category = category
        self.serial_number = serial_number
        self.net = net
        self.vat = vat
        self.date_of_purchase = datetime.strptime(date_of_purchase, "%Y-%m-%d")
        self.date_of_transaction = datetime.strptime(date_of_transaction, "%Y-%m-%d")
        self.shop_name = shop_name

