from pydantic import BaseModel, EmailStr, AnyUrl, Field, Optional

class Patient(BaseModel):
  name: str
  age : int
  mail = EmailStr                           #  (Email validation)
  dic : list[str]                     #  (Multi layer validation)
  allergies : Optional[int] #  (Optional field)
  linkedin : AnyUrl                         #  (URL validation)



def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print("Inserted patient data")

patient_info = {"name": "Ananya", "age": 89}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

