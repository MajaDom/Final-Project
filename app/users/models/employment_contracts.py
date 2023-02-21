from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Date, Float, Boolean, Integer
from app.db import Base


class EmploymentContract(Base):
    __tablename__ = "employment_contracts"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id_row = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    contract_type = Column(String(50), nullable=False)
    paycheck = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)

    fk_employee_id = Column(Integer, ForeignKey("employees.id_employee"), nullable=False)

    def __init__(self, start_date, end_date, contract_type, paycheck, is_active, fk_employee_id):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date is None or end_date == "":
            self.end_date = end_date
        else:
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.contract_type = contract_type
        self.paycheck = paycheck
        self.is_active = is_active
        self.fk_employee_id = fk_employee_id
