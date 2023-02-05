from sqlalchemy import Column, String, Boolean
from uuid import uuid4
from app.db import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(String(50), primary_key=True, default=uuid4)
    user_name = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password