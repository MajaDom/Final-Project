from sqlalchemy import Column, String, Integer
from app.db import Base


class Client(Base):
    __tablename__ = "clients"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String(100), nullable=False, unique=True)
    contact = Column(String(50), unique=True, nullable=False)

    def __init__(self, client_name, contact):
        self.client_name = client_name
        self.contact = contact
