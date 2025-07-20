from fastapi import FastAPI, Path, HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,computed_field
from typing import Annotated,Literal
import json 
import os 

app = FastAPI()

class Pateint(BaseModel):

    id:Annotated[str,Field(...,description='ID of the Patient',examples=['P001'])]
    name:Annotated[str,Field(...,description='Name of the patient')]
    city:Annotated[str,Field(...,description='city where the patient is living')]
    age:Annotated[int,Field(...,gt=0,lt=120,description='age of the patient')]
    gender:Annotated[Literal['male','female','others'],Field(...,description='gender of the patient')] 
    height:Annotated[float,Field(...,gt=0,description='Height of the patient in ,mtrs')]
    weight:Annotated[float,Field(...,gt=0,description='weight of the patient in kgs')] 

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi 
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi<18.5:
            return "Underweight"
        elif self.bmi<30:
            return 'Normal'
        else:
            return 'Obese'


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "02_patients.json")
    with open(file_path,'r') as file:
        data=file.read()
    data=json.loads(data)
    return data 

def save_data(data):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "02_patients.json")
    with open(file_path,'w') as file:
        json.dump(data,file)



@app.get("/")
def hello():
    return {"message": "Patient Management System API."}


@app.get("/about")
def about():
    return {"message":"A fully functional API to manage your patient records."}

@app.get("/view")
def view():
    data=load_data()
    return data 


@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description="ID of the existing patient",
                                     example='P001')):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail="Patient not Found!") 
    

@app.get('/sort')
def sort_patient(sort_by: str=Query(...,description="Sort on the basis of height,weight or bmi")
                 , order:str=Query('asc',description="Sort in ascending or descending")):
    
    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order select between asc and desc')
    
    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(), key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data 

@app.post('/create')
def create_patient(patient:Pateint):
    data=load_data()
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exist')
    else:
        data[patient.id]=patient.model_dump(exclude=['id'])

        save_data(data)

        return JSONResponse(status_code=201,content={'message':'Patient created successfully.'})