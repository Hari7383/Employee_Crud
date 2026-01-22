from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee CRUD API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)

@app.get("/employees", response_model=list[schemas.EmployeeOut])
def read_employees(
    skip: int = 0,
    limit: int = Query(default=10, le=50),
    search: str | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_employees(db, skip, limit, search)

@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, emp: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    employee = crud.update_employee(db, emp_id, emp)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}


@app.get("/")
def root():
    return {"status": "Employee CRUD API running"}
