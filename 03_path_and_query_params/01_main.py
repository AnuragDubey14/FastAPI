from fastapi import FastAPI
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
def view_patient(patient_id:str):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"error":"Patient not found."}