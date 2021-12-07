from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import Date
from .database import Base

class Emp(Base):
    __tablename__ = "EmployeeTable"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    desig = Column(String)
    present = Column(Boolean)
    doj = Column(Date)
