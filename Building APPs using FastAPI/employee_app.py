from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List
employee_db: List[Employee] = []
app = FastAPI()

#1-Read all employees
@app.get('/employees', response_model=List[Employee])
def get_employees():
    return employee_db

#2. Read specific employee
@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee(emp_id: int):
    for employee in employee_db:
        if employee.id == emp_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee Not found")

#3. Create employee
@app.post('/employees', response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employee_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with given ID already exists")
    employee_db.append(new_emp)
    return new_emp

#4. Update an employee
@app.put('/employees/{emp_id}', response_model=Employee)
def update_employee(emp_id: int, updated_emp: Employee):
    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            employee_db[index] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404, detail="Employee Not found")

#5 Delete an employee
@app.delete('/employees/{emp_id}')
def delete_employee(emp_id:int):
    for index,employee in enumerate(employee_db):
        if employee.id ==emp_id:
            del employee_db[index]
            return {'message':'Employee deleted successfully'}
    raise HTTPException(status_code=404, detail="Employee Not found")
