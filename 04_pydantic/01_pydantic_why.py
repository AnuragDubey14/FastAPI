from pydantic import BaseModel, EmailStr, AnyUrl, Field 
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50, title='name of the patient',description='Give the name of the patient in less than 50 character',examples=['anurag'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age: int = Field(gt=0,lt=120)
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=False,description="Is the Patient Married or not")]# default value
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)] # default and optional
    contact_details: Dict[str,str]


patient_info={'name':'ABCD','email':'abc@gmail.com',
              "linkedin_url":"http://linkedin.com/1322",'age':30,'weight':60,
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

