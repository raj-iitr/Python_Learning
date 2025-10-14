from pydantic import BaseModel

class Patient(BaseModel):

  name: str
  age : int

def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print("Inserted patient data")

patient_info = {"name": "Ananya", "age": "89"}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

