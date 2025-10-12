 ##How to read a text file in python

 file_path = "temp1.txt"

 try:
   with open(file_path, "r") as file:
     content = file.read()
     print(content)
 except FileNotFoundError:
    print(f"{file_path} does not exist.")


######################################################
# How to read a json file in python

import json

file_path = "temp1.json"

try:
  with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
    print(content['city'])
except FileNotFoundError:
   print(f"{file_path} does not exist.")

######################################################
# How to read a csv file in python

import csv

file_path = "temp1.csv"

try:
  with open(file_path, "r") as file:
    content = csv.reader(file)
    for line in content:
      print(line[0])
except FileNotFoundError:
   print(f"{file_path} does not exist.")
