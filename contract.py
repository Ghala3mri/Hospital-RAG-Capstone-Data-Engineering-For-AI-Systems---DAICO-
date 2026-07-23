from pydantic import BaseModel, Field
from typing import Optional

class HealthcareRecord(BaseModel):
    Name: str
    Age: int = Field(ge=0, le=120)
    Gender: str
    Blood_Type: str
    Medical_Condition: str
    Date_of_Admission: str
    Doctor: str
    Hospital: str
    Insurance_Provider: str
    Billing_Amount: float
    Room_Number: int
    Admission_Type: str
    Discharge_Date: Optional[str]
    Medication: Optional[str]
    Test_Results: Optional[str]