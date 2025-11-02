from fastapi import FastAPI , Path , HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from typing import Annotated , Literal
import json

app = FastAPI() 
 
class Patient(BaseModel):
    id : Annotated[str , Field(... , description = 'ID of the patient' , examples=['P001'])] 
    name: Annotated[str , Field(... , description = 'Name of the patient' , examples = ['Aryan Dwivedi'])]
    city: Annotated[str , Field(... , description = 'City of the patient' , examples= ['New York'])]
    age : Annotated[int , Field(... , gt = 0 , lt =120 , description = 'Age of the patient' , examples = [25] )]
    gender : Annotated[Literal['male','female' , 'others'] , Field(... , description = 'Gender of the patient')]
    height : Annotated[float , Field(... , gt = 0 , lt = 250 , description = 'Height of the patient in cm' , examples = [175.5] )]
    weight : Annotated[float , Field(... , gt = 0 , lt = 300 , description = 'Weight of the patient in kg' , examples = [70.5] )]

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        bmi_value = self.weight / (height_in_meters ** 2)
        return round(bmi_value , 2)
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 24.9:
            return "Normal weight"
        elif self.bmi < 29.9:
            return "Overweight"

def load_data():
    with open("project.json" , "r") as f:
        data = json.load(f)
        return data
    
def save_data(data):
     with open('project.json' , 'w') as f:
         json.dump(data , f)   

@app.get("/")
def read_root():
    return {"message": "hello from fast api"}

@app.get("/about")
def read_about():
    return {"message": "this is a fastapi project"}

@app.get("/patients")
def read_patients():
    data = load_data()
    return data
@app.get("/patients/{patient_id}")
def read_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve" , example = "P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient not found")

@app.post("/create_patient")
def create_patient(patient: Patient):

    # load existing data 
    data = load_data()
    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code= 400 , detail = 'patient already exists')
     # new patient add to the data base
    data[patient.id] = patient.model_dump(exclude = ['id']) 

    # save the updated data back to the json file
    save_data(data)
    return JSONResponse(content={"message": "Patient created successfully"}, status_code=201)
    