from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

from .database import Base, table_name


class ContiModel(Base):
    __tablename__ = table_name
    __table_args__ = ({"mysql_engine": "Aria"},)

    id = Column(Integer, autoincrement=True, primary_key=True)
    date_time = Column(DateTime, default=(datetime.utcnow()))
    flag = Column(String(64), unique=False, nullable=False, index=True)
    prompt = Column(String(512), unique=False, nullable=False)
    model = Column(String(64), unique=False, nullable=False)
    response = Column(String(512), unique=False, nullable=False)
    elapsed_seconds = Column(Float, unique=False, nullable=False)
