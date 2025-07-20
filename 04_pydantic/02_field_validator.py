from pydantic import BaseModel, EmailStr, AnyUrl, Field , field_validator,model_validator,computed_field
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50, title='name of the patient',description='Give the name of the patient in less than 50 character',examples=['anurag'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age: int = Field(gt=0,lt=120)
    height:float #meter
    weight: Annotated[float,Field(gt=0,strict=True)]  #KG's
    married: Annotated[bool,Field(default=False,description="Is the Patient Married or not")]# default value
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)] # default and optional
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi 


    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact number.')
        return model
        


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains =['hdfc.com','icici.com']

        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()


patient_info={'name':'abcd','email':'abc@hdfc.com',
              "linkedin_url":"http://linkedin.com/1322",'age':65,'height':1.6,'weight':60,
              'married':True,
              'allergies':['pollen','dust'],
              'contact_details':{'email':'abc@gmail.com','phone':'0123456789','emergency':'1234551438'}}

patient1=Patient(**patient_info)


def update_patient_data(patient:Patient):
    "Type hinting is not generate error in python."
    print(patient.name)
    print(patient.age)
    print("BMI-->",patient.bmi)
    print("inserted into database.")

update_patient_data(patient1)
