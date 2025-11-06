from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd


#import the ml model
with open('regmodel.pkl' , 'rb') as f:
    model = pickle.load(f)

app =  FastAPI()

#pydentic model to validate the given data 
class UserInput(BaseModel):
    MedInc:  Annotated[float , Field(... ,gt=0 , description= "Median Income in block group")]
    HouseAge:Annotated[float , Field(...,gt=0 , description = "Median house age in block group")]
    AveRooms: Annotated[float , Field(...,gt=0 , description = "Average number of rooms per household")]
    AveBedrms:Annotated[float , Field(..., gt=0 , description= "Average number of bedrooms per household")]
    Population:Annotated[float , Field(... ,gt=0 , description = "Block group population")]
    AveOccup: Annotated[float , Field(... ,gt=0 , description = "Average number of household members")]
    Latitude: Annotated[float , Field(... ,ge=-90 , le=90 , description = "Latitude: ")]
    Longitude:Annotated[float , Field(...,ge=-180 , le=180 , description = "Longitude: ")]


# now we will create an endpoint for prediction
@app.post('/predict')
def predict_price(data: UserInput):
    input_df =pd.DataFrame([{
        'MedInc': data.MedInc,
        'HouseAge': data.HouseAge,
        'AveRooms': data.AveRooms,
        'AveBedrms': data.AveBedrms,
        'Population': data.Population,
        'AveOccup': data.AveOccup,
        'Latitude': data.Latitude,
        'Longitude': data.Longitude
    }])

    prediction =model.predict(input_df)[0]

    return JSONResponse(status_code = 200 , content = {'predicted_price': prediction})