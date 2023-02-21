from sqlalchemy import Column, Integer, String
from app.db import Base


class Supplier(Base):
    __tablename__ = "suppliers"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(100), nullable=False, unique=True)
    contact = Column(String(50), unique=True, nullable=False)

    def __init__(self, supplier_name, contact):
        self.supplier_name = supplier_name
        self.contact = contact
