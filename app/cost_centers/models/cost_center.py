# The CostCenter class is a model that represents a cost center.
from sqlalchemy import Column, String, Integer
from app.db import Base


class CostCenter(Base):
    __tablename__ = "cost_centers"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    cost_center_id = Column(Integer, primary_key=True, autoincrement=True)
    center_name = Column(String(100), nullable=False, unique=True)
    center_code = Column(String(50), nullable=False, unique=True)

    def __init__(self, center_name, center_code):
        self.center_name = center_name
        self.center_code = center_code
