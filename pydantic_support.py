from pydantic import BaseModel, EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated



class Patient(BaseModel):
    name : Annotated[str,  Field(default = 'Admin',min_length = 3 , max_length = 50 , title= "Name of the patient" ,description = "Full name of the patient" , example= ['Aryan Dwivedi', 'Reshu'])]
    age : Annotated[int , Field(gt = 0 , lt = 150 , strict=True)]  # <---- age should be greater than 0 and less than 150
    email : EmailStr 
    linkedin_url : AnyUrl
    weight : float= Field(gt = 0 ,ls =120)  # <---- weight should be greater than 0 and less than 120
    married : Optional[bool] = None  # <---- optional boolean field
    alergies : List[str]= Field(min_length = 1 , max_length = 10) # <---- list of string 
    contact_detalis : Dict[str , str]  # <---- dictionary with string keys and string values

def insert_patient(patient : Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.email)
    print(patient1.linkedin_url)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.alergies)
    print(patient1.contact_detalis)

patient_info = {'name':'Aryan','age': 18 , 'email': 'aryan@gmail.com' ,'linkedin_url': 'https://www.linkedin.com/in/aryan-dwivedi-/' , 'weight': 70.5 , 'married': False , 'alergies': ['pollen' , 'nuts'] , 'contact_detalis': {'phone': '1234567890' , 'email':''}}
patient1 = Patient(**patient_info)

insert_patient(patient1)