from app.db import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id_employee = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    contact = Column(String(50), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=True, unique=True)

    def __init__(self, first_name, last_name, contact, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.user_id = user_id
