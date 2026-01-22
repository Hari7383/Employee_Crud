from sqlalchemy.orm import Session
from . import models, schemas
import app

def create_employee(db: Session, emp: schemas.EmployeeCreate):
    employee = models.Employee(**emp.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employees(db: Session, skip=0, limit=10, search=None):
    query = db.query(models.Employee)
    if search:
        query = query.filter(models.Employee.name.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()

def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()

def update_employee(db: Session, emp_id: int, emp: schemas.EmployeeUpdate):
    employee = get_employee(db, emp_id)
    if not employee:
        return None
    for key, value in emp.dict().items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(db: Session, emp_id: int):
    employee = get_employee(db, emp_id)
    if not employee:
        return None
    db.delete(employee)
    db.commit()
    return employee

