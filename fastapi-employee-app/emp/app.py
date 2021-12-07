from os import name
from fastapi import FastAPI, Depends
from . import schemas, models
from .utils import add_emp, get_all_emp, show_emp
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind = engine)
 
@app.get("/")
async def root():
    return {"data":"Welcome to homepage"}

@app.post("/create")
async def create_emp(request : schemas.Employee, db : Session = Depends(get_db)):
    new_emp = add_emp(request, db)
    return new_emp

@app.get("/allemps")
async def show_emps(db : Session = Depends(get_db)):
    all_emps = get_all_emp(db)
    return all_emps

@app.get("/emp/{emp_id}")
async def get_emp(emp_id: int, db : Session = Depends(get_db)):
    emp = show_emp(emp_id, db)
    return emp

