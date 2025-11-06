from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/", response_model=List[schemas.EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, emp_id=emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db=db, emp_id=emp_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    if not crud.delete_employee(db=db, emp_id=emp_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}