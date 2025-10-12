######################################################
# By using this method one can write  data to a file and also handle the error if the file already exists.
# w = write
# x = create
# a = append

txt_data = "I like Pizza"
file_path = "temp1.py"

try:
  with open(file_path, "a") as file:
    file.write(txt_data)
    print(f"Data written to {file_path}")
except FileExistsError:
  print(f"{file_path} already exists. Data not written.")



##########################################################
#This is a way to write a list of data to a file and also handle the error if the file already exists.
  
txt_data = ["Tyrion Lennister", "Daenerys Targaryen","Jon Snow","Arya Stark","Sansa Stark","Jaime Lennister","Cersei Lennister","Joffrey Baratheon","Sandor Clegane","Theon Greyjoy","Bran Stark","Brienne of Tarth","Missandei",]

file_path = "temp1.py"

try:
  with open(file_path, "a") as file:
    for item in txt_data:
      file.write(item + "\n")
    print(f"Data written to {file_path}")
except FileExistsError:
  print(f"{file_path} already exists. Data not written.")



##########################################################
# for json file

import json

txt_data = {
   "name": "Tyrion Lennister",
   "age" : 30,
   "city": "Kings Landing"
}

file_path = "temp1.json"

try:
  with open(file_path, "w") as file:
    json.dump(txt_data,file, indent=4)
    print(f"Data written to {file_path}")
except FileExistsError:
  print(f"{file_path} already exists. Data not written.")


##########################################################
# .csv file


import csv

txt_data = [
  ["Name", "Age", "Job"],
  ["Tyrion Lennister", 30, "Hand of the Queen"],
  ["Daenerys Targaryen", 20, "Mother of Dragons"],
  ["Jon Snow", 25, "King in the North"],
  ["Arya Stark", 18, "No One"],
  ["Sansa Stark", 17, "Lady of Winterfell"],
  ["Jaime Lennister", 35, "Kingsguard"],
  ["Cersei Lennister", 35, "Queen of the Seven Kingdoms"],
  ["Joffrey Baratheon", 18, "King of the Seven Kingdoms"],
  ["Sandor Clegane", 35, "The Hound"],
  ["Theon Greyjoy", 25, "Reek"],
  ["Bran Stark", 15, "Three-Eyed Raven"],

]

file_path = "temp1.csv"

try:
  with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in txt_data:
      writer.writerow(row)
    print(f"Data written to {file_path}")
except FileExistsError:
  print(f"{file_path} already exists. Data not written.")


##########################################################
