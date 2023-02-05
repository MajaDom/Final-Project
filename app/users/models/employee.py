from uuid import uuid4
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Employee(Base):
    __tablename__ = "employees"
    id_employee = Column(String(50), primary_key=True, default=uuid4)
    first_name = Column(String(50))
    last_name = Column(String(50))

    user_id = Column(String(50), ForeignKey("users.user_id"))
