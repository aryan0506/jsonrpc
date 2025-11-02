from pydantic import BaseModel, EmailStr, AnyUrl,model_validator
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

    @model_validator(mode = 'after')
    
    def validate_emergency_concept(cls , model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years')
        return model




def insert_patient(patient: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.email)
    print(patient1.linkedin_url)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.alergies)
    print(patient1.contact_details)


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
