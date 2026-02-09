# Employee CRUD API

A lightweight **RESTful API** for managing employee records built with **Flask**.  
This project demonstrates clean backend API design with **CRUD (Create, Read, Update, Delete)** functionality — a fundamental building block in real-world applications.

---

## 🚀 Project Overview

This repository implements:
✔ A Flask API  
✔ Endpoints for employee management  
✔ JSON-based request/response  
✔ Basic data storage (in-memory or simple file)  
✔ Structured code for learning and extension

This serves as a foundation for:
- Backend microservices
- API backend for web or mobile apps
- Scaling to databases (PostgreSQL, MongoDB)
- Authentication / role-based access

---

## 🧠 Features

| Feature | Description |
|---------|-------------|
| Create Employee | Add a new employee |
| Read All Employees | Retrieve all records |
| Read Single Employee | Get details by ID |
| Update Employee | Modify existing record |
| Delete Employee | Remove record by ID |

---

## 🛠️ Tech Stack

- Python 3.8+
- Flask
- Flask-RESTful (optional)
- Pip for package management

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Hari7383/Employee_Crud.git
cd Employee_Crud
```

employee_crud/

│

├── app/

│   ├── __init__.py   ← (empty file)

│   ├── main.py          # FastAPI entry point

│   ├── database.py      # DB connection

│   ├── models.py        # SQLAlchemy models

│   ├── schemas.py       # Pydantic schemas (validation)

│   └── crud.py          # DB operations

│

├── tests/

│   ├── __init__.py  ← (empty file)

│   └── test_employee.py # Pytest cases

│

├── requirements.txt

└── README.md

### Environment Setup & Run Instructions: 

1️⃣ Create virtual environment (recommended) : 
```
python -m venv venv
source venv/bin/activate   # Mac / Linux
venv\Scripts\activate      # Windows
```

### Project Setup

3️⃣ Install Dependencies : 
```
pip install -r requirements.txt
```

### Testing 

4️⃣ Run Unit Tests : 
```
pytest
```

### Run the Application 

5️⃣ Start FastAPI Server : 
```
uvicorn app.main:app --reload
```


### Access the API 

6️⃣ Open Swagger UI (API Documentation) :
```
http://127.0.0.1:8000/docs
```

Note:
The root URL http://127.0.0.1:8000/ will not display the API documentation.
You must manually append /docs to access the Swagger UI.
