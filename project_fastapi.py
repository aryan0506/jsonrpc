from fastapi import FastAPI , Path , HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from typing import Annotated , Literal , Optional
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
        

class PatientUpdate(BaseModel): # This model will be use when we want to update our patient data 
    name : Annotated[Optional[str] , Field(default=None)]
    city : Annotated[Optional[str], Field(default = None)]
    age : Annotated[Optional[int], Field(default = None , gt=0)]
    gender: Annotated[Optional[Literal['male' , 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None , gt = 0)]
    weight: Annotated[Optional[float], Field(default=None, gt = 0)]



def load_data():# this function will be use when we want to load the data from database 
    with open("project.json" , "r") as f:
        data = json.load(f)
        return data
    
def save_data(data): # this function will be use when we want to post data in our database
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

# this endpoint will going to handle updating patient detail
@app.put("/edit/{patient_id}")
def update_patient(patient_id:str , patient_update: PatientUpdate):
     
     # load data
      data = load_data()
     
     # check if patient exists

      if patient_id not in data:
          raise HTTPException(status_code=404 , detail = 'patient not found')
      
      existing_patient_info = data[patient_id] 

      updated_patient_info = patient_update.model_dump(exclude_unset= True)

      for key , value in updated_patient_info.items():
          existing_patient_info[key] = value
      existing_patient_info['id'] = patient_id
      patient_pydantic_obj = Patient(**existing_patient_info)
      existing_patient_info = patient_pydantic_obj.model_dump(exclude = 'id')


      data[patient_id] = existing_patient_info

      # save data
      save_data(data)

      return JSONResponse(content={"message": "Patient updated successfully"}, status_code=200)

# this endpoint will going to handle deleting patient detail

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    # check if patient exists
    if patient_id not in data:
        raise HTTPException(status_code = 404 , detail = 'patient not found')
    
    del data[patient_id]

    save_data(data)
    return JSONResponse(content={"message": "Patient deleted successfully"}, status_code=200)




       