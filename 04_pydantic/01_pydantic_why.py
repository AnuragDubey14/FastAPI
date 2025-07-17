from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int 
    weight: float
    married: bool = False # default value
    allergies: Optional[List[str]]=None # default and optional
    contact_details: Dict[str,str]


patient_info={'name':'ABCD','age':30,'weight':60,
              'married':True,
              'allergies':['pollen','dust'],
              'contact_details':{'email':'abc@gmail.com','phone':'0123456789'}}

patient1=Patient(**patient_info)


def insert_patient_data(name:str,age:int):
    "Type hinting is not generate error in python."
    print(name)
    print(age)
    print("inserted into database.")

insert_patient_data('abcd',30)


def update_patient_data(patient:Patient):
    "Type hinting is not generate error in python."
    print(patient.name)
    print(patient.age)
    print("inserted into database.")

update_patient_data(patient1)

