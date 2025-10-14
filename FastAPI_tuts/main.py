from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json


app = FastAPI()

class Patient(BaseModel):
  id: Annotated[str, Field(description="ID of the patient", examples=["P001"])]
  name: Annotated[str, Field(description="name of the patient")]
  age: Annotated[int, Field(...,gt=0,lt=120,description="age of the patient")]
  city: Annotated[str, Field(description="city of the patient")]
  gender:Annotated[Literal["Male","Female","Others"], Field(description="name of the patient")]
  height:Annotated[float, Field(gt=0,description="name of the patient")]
  weight: Annotated[float, Field(gt=0,description="name of the patient")]

  @computed_field
  @property
  def bmi(self) -> float:
    bmi = round(self.weight / (self.height ** 2), 2)
    return bmi

  @computed_field
  @property
  def verdict(self) -> str:
    if self.bmi < 18.5:
      return "Underweight"
    elif self.bmi < 30:
      return "Normal"
    else:
      return "Overweight"
  

def load_data():
  with open("patients.json", "r") as f:
    data = json.load(f)
    return data

def save_data(data):
  with open("patients.json", "w") as f:
    json.dump(data, f, indent=4)

@app.get("/")
def test():
  return {"message": "Patient Management System API"}

@app.get("/view")
def view():
   data = load_data()
   return data 

# Use of Path parameter

@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient to view", example="P001")):
  data = load_data()
  if patient_id in data:
     return data[patient_id]
  raise HTTPException(status_code=404, detail="Patient not found")

# Use of Query parameter

@app.get("/sort")
def sort_patients(sort_by : str = Query(...,description="Sort on the basis of height, weight, bmi"), order : str = Query('asc', description="sort in asc or desc order")):

  valid_fields = ['height', 'weight', 'bmi']

  if sort_by not in valid_fields:
    raise  HTTPException(status_code=400, detail="Invalid sort field {valid_fields}")

  if order not in ['asc', 'desc']:
    raise HTTPException(status_code=400, detail="Invalid order. Use 'asc' or 'desc'")

  data = load_data()

  sort_order = False if order == 'asc' else True

  sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)

  return sorted_data


@app.post("/create")
def create_patient(patient: Patient):
   # load existing data
   data = load_data()

   # check if patient already exists
   if patient.id in data:
       raise HTTPException(status_code=400, detail="Patient already exists")

   # Add new patient to the database
   data[patient.id] = patient.model_dump(exclude={"id"})

   # Save the updated data to the JSON file
   save_data(data)

   return JSONResponse(content={"message": "Patient created successfully"}, status_code=201)