from pydantic import BaseModel, EmailStr, AnyUrl, model_validator,computed_field
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float
    married: Optional[bool] = None  # <---- optional boolean field
    alergies: List[str]  # <---- list of string
    contact_details: Dict[str, str]

    
    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.weight / 100  # assuming weight is in kg and height is in cm
        bmi_value = self.weight / (height_in_meters ** 2)
        return round(bmi_value, 2)


def insert_patient(patient: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.email)
    print(patient1.linkedin_url)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.alergies)
    print(patient1.contact_details)
    print("BMI:", patient1.bmi)


patient_info = {
    "name": "Aryan",
    "age": 18,
    "email": "aryan@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/aryan-dwivedi-/",
    "weight": 70.5,
    "married": False,
    "alergies": ["pollen", "nuts"],
    "contact_details": {"phone": "1234567890"},
}
patient1 = Patient(**patient_info)

insert_patient(patient1)
