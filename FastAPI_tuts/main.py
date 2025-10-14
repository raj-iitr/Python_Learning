from fastapi import FastAPI, HTTPException, Path, Query
import json


app = FastAPI()

def load_data():
  with open("patients.json", "r") as f:
    data = json.load(f)
    return data

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