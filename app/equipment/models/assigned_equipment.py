from datetime import datetime
from sqlalchemy import Column, Integer, Date, ForeignKey
from app.db import Base


class AssignedEquipment(Base):
    __tablename__ = "assigned_equipment"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    assigned_equipment_id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    id_employee = Column(Integer, ForeignKey("employees.id_employee"), nullable=False)
    equipment_id = Column(Integer, ForeignKey("equipment.equipment_id"), nullable=False)

    def __init__(self, start_date, end_date, id_employee, equipment_id):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date is None:
            self.end_date = end_date
        else:
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.id_employee = id_employee
        self.equipment_id = equipment_id
