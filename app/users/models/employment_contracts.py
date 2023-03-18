# EmploymentContract is a class that represents a table in the database
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Date, Float, Boolean, Integer, CheckConstraint
from sqlalchemy.orm import relationship

from app.db import Base


class EmploymentContract(Base):
    __tablename__ = "employment_contracts"
    __table_args__ = (
        CheckConstraint("contract_type IN ('full-time', 'part-time')", name="contract_type_constraint"),
        CheckConstraint("end_date is NULL or end_date > start_date", name="check_dates"),
        CheckConstraint("end_date is NULL or end_date > termination_date > start_date", name="check_termination_date"),
        CheckConstraint("paycheck > 0", name="paycheck_greater_then_zero"),
        {"mysql_engine": "InnoDB"},
    )

    id_row = Column(Integer, primary_key=True, autoincrement=True)
    contract_type = Column(String(50), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    paycheck = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    termination_date = Column(Date)
    description_contract = Column(String(500))

    fk_employee_id = Column(Integer, ForeignKey("employees.id_employee"), nullable=False)
    owner = relationship("Employee", back_populates="contracts")

    def __init__(self, start_date, end_date, contract_type, paycheck, termination_date, description_contract,
                 fk_employee_id):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date is not None:
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        else:
            self.end_date = end_date
        self.contract_type = contract_type
        self.paycheck = paycheck
        if termination_date is not None:
            self.termination_date = datetime.strptime(termination_date, "%Y-%m-%d")
        else:
            self.termination_date = termination_date
        self.description_contract = description_contract
        self.fk_employee_id = fk_employee_id
