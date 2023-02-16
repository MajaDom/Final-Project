from app.db import Base
from sqlalchemy import Column, Integer, String, Boolean


class Supplier(Base):
    __tablename__ = "suppliers"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(100), nullable=False)
    contact = Column(String(50), unique=True, nullable=False, )
    is_active = Column(Boolean, default=True)

    def __init__(self, supplier_name, contact):
        self.supplier_name = supplier_name
        self.contact = contact
