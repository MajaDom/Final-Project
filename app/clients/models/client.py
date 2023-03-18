# It's a class that represents a client
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db import Base

# The Client class is a Python class that inherits from the Base class. It has a client_id, client_name, and contact
# attribute


class Client(Base):
    __tablename__ = "clients"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), unique=True)

    client_contract = relationship("ClientContract", back_populates="client")

    def __init__(self, client_name, contact):
        self.client_name = client_name
        self.contact = contact
