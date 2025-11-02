from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional


class Adress(BaseModel):
    city: str
    state: str
    pincode: str


class Patient(BaseModel):
    name: str
    age: int
    email: str
    address: Adress


address_dict = {"city": "Mumbai", "state": "Maharashtra", "pincode": "400001"}
address1 = Adress(**address_dict)

patient_dict = {
    "name": "John",
    "age": 30,
    "email": "XXXXXXXXXXXXXX",
    "address": address1,
}
patient1 = Patient(**patient_dict)

temp = patient1.model_dump_json()
print(temp)
