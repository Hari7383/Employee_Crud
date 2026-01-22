from pydantic import BaseModel, Field, field_validator
import re
from pydantic import ConfigDict

class EmployeeBase(BaseModel):
    name: str
    address: str
    salary: float = Field(gt=0)
    age: int = Field(gt=0)

    @field_validator("name")
    @classmethod
    def name_validation(cls, v):
        import re
        if not re.match(r"^[A-Za-z ]+$", v):
            raise ValueError("Name must contain only letters and spaces")
        return v

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     from_attributes = True
