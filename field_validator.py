from pydantic import BaseModel, EmailStr, AnyUrl , field_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age:  int
    email : EmailStr
    linkedin_url: AnyUrl
    weight: float 
    married: Optional[bool] = None  # <---- optional boolean field
    alergies: List[str] # <---- list of string
    contact_detalis: Dict[
        str, str
    ]  
    @field_validator('email')
    @classmethod
    def email_validator(cls , value):
        valid_domain = ['hdfc.com' , 'icici.com' , 'sbi.com', 'gmail.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Email domain is not valid')
        return value
    
    @field_validator('name' , mode = 'after')
    @classmethod
    def name_convertor(cls , value):
        return value.upper()

def insert_patient(patient: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.email)
    print(patient1.linkedin_url)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.alergies)
    print(patient1.contact_detalis)


patient_info = {
    "name": "Aryan",
    "age": 18,
    "email": "aryan@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/aryan-dwivedi-/",
    "weight": 70.5,
    "married": False,
    "alergies": ["pollen", "nuts"],
    "contact_detalis": {"phone": "1234567890", "email": ""},
}
patient1 = Patient(**patient_info)

insert_patient(patient1)
