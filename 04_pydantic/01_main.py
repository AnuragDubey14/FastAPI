from fastapi import FastAPI, Path, HTTPException,Query
import json 
import os 

app = FastAPI()

def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "02_patients.json")
    with open(file_path,'r') as file:
        data=file.read()
    data=json.loads(data)
    return data 

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