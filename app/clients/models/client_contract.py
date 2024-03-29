# The ClientContract class is a representation of the client_contracts table in the database
from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


# > This class is a representation of a client contract
class ClientContract(Base):
    __tablename__ = "client_contracts"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    client_contract_id = Column(Integer, primary_key=True, autoincrement=True)
    contract_code = Column(String(100), unique=True, nullable=False)
    start_date = Column(Date, nullable=False)
    contract_description = Column(String(500))
    end_date = Column(Date, nullable=True)

    client_id = Column(Integer, ForeignKey("clients.client_id"), nullable=False)
    client = relationship("Client", back_populates="client_contract")

    def __init__(self, contract_code, start_date, contract_description, end_date, client_id):
        self.contract_code = contract_code
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.contract_description = contract_description
        if end_date is None:
            self.end_date = end_date
        else:
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.client_id = client_id
