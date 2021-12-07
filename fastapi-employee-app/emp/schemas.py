from pydantic import BaseModel
from datetime import date, datetime

class Employee(BaseModel):
    ename : str
    designation : str
    present : bool
    doj : date