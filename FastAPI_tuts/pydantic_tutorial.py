from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Optional, List, Dict,

class Patient(BaseModel):
  name: str
  age : int
  mail = EmailStr                           #  (Email validation)
  dic : List[str]                     #  (Multi layer validation)
  allergies : Optional[int]            #  (Optional field)
  linkedin : AnyUrl                         #  (URL validation)
  weight = Field(gt)



def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print("Inserted patient data")

patient_info = {"name": "Ananya", "age": 89}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

