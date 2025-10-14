from pydantic import BaseModel, EmailStr, AnyUrl,  Field, field_validator, model_validator, computed_field
from typing import Optional, List, Dict, Annotated

class Address(BaseModel):
  city : str
  state : str
  pin : str


class Patient(BaseModel):
  name: str
  age : int
  address : Address
  mail: EmailStr                           #  (Email validation)
  dic : List[str]                          #  (Multi layer validation)
  allergies : Optional[int] = None         #  (Optional field)
  linkedin : AnyUrl                         #  (URL validation)
  weight : float = Field(gt=0, lt=100)      #  (Field validation)
  height : Annotated[float, Field(gt=0, lt=3, description="Height in meters")] #Field function help in attaching metadata                                                                                 as well as default value too
  length : float = Field(strict=True)       #No type coersion (No conversion of int to float or str to int)



  #Field validation

  # This method is used to validate the email field
  # Field operator can be operated in two mode =
  # 1) Before = it will take before type coersion value
  # 2) After = it will take after type coersion value
  # The default mode is "after"

  @field_validator("mail", mode="after")
  @classmethod 
  def email_validator(cls, value):
    valid_domains = ["gmail.com", "yahoo.com"]
    domain_name = value.split("@")[-1]

    if domain_name not in valid_domains:
      raise ValueError("Invalid domain name")

    return value


  #Model validation
  # it operates on the whole model (multiple fields))
  @model_validator(mode="after")
  def validate_emergency_contact(self):
    if self.age > 60 and hasattr(self, 'contact_details') and 'emergency_contact' not in self.contact_details:
      raise ValueError("Emergency contact is required for patients above 60 years")
    return self

  #Computed field
  # It is used to calculate the value of a field based on the value of other fields
  @computed_field
  @property
  def bmi(self) -> float:
    bmi = round(self.weight / (self.height ** 2), 2)
    return bmi


address_dict = {"city": "Guwahati", "state": "Assam", "pin": "781001"}
address1 = Address(**address_dict)

patient_dict = {"name": "Ananya", "age": 89, "address": address1, "mail": "ananya@gmail.com", "dic": ["a", "b", "c"], "linkedin":"https://linkedin.com/in/ananya", "weight": 90, "height": 1.65, "length": 1.65}
patient1 = Patient(**patient_dict)

print(patient1)




def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print("Inserted patient data")

# patient_info = {"name": "Ananya", "age": 89}

# patient1 = Patient(**patient_info)

insert_patient_data(patient1)

