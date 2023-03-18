# The Employee class is a model that represents the employees table in the database
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from app.db import Base


class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id_employee = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100))
    phone_number = Column(String(25), nullable=False)
    is_active = Column(Boolean, default=True)

    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=True, unique=True)
    contracts = relationship("EmploymentContract", back_populates="owner")

    def __init__(self, first_name, last_name, email, phone_number, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.user_id = user_id
