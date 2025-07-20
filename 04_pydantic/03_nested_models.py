from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str 
    pin:str 

class Patient(BaseModel):

    name:str
    gender: str
    age: int 
    address:Address


address_dict={'city':'Gurugram','state':'Haryana',"pin":"122011"}

address1=Address(**address_dict)

patient_dict={'name':'abcd','gender':'male','age':25,'address':address1}


patient1=Patient(**patient_dict)

print("Name->",patient1.name)
print("gender->",patient1.gender)
print("age->",patient1.age)
print("city->",patient1.address.city)
print("state->",patient1.address.state)
print("pin->",patient1.address.pin)

temp=patient1.model_dump(include=['name','gender'],exclude=['age'])
temp1=patient1.model_dump_json()

print(type(temp))
print(type(temp1))

