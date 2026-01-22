# Employee_Crud

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

1️⃣ Create Virtual Environment: 
python -m venv env

2️⃣ Activate Virtual Environment (Windows): 
env\Scripts\activate


# Project Setup

3️⃣ Install Dependencies: 
pip install -r requirements.txt


# Testing 

4️⃣ Run Unit Tests: 
pytest


# Run the Application 

5️⃣ Start FastAPI Server: 
uvicorn app.main:app --reload


# Access the API 

6️⃣ Open Swagger UI (API Documentation): 
http://127.0.0.1:8000/docs

Note:
The root URL http://127.0.0.1:8000/ will not display the API documentation.
You must manually append /docs to access the Swagger UI.
