from app.db import Base
from sqlalchemy import Column, String, Integer, Boolean


class CostCenter(Base):
    __tablename__ = "cost_centers"
    __table_args__ = {'mysql_engine': 'InnoDB'}

    cost_center_id = Column(Integer, primary_key=True, autoincrement=True)
    center_name = Column(String(100), nullable=False)
    center_code = Column(String(50), nullable=False)  # todo perhaps add unique, check
    is_active = Column(Boolean, default=True)

    def __init__(self, center_name, center_code):
        self.center_name = center_name
        self.center_code = center_code
